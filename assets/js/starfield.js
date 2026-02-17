(() => {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const root = document.documentElement;

  const rand = (min, max) => Math.random() * (max - min) + min;

  const colorVars = ["--bg-star-1", "--bg-star-2", "--bg-star-3"];
  const accentColorVars = ["--accent-coral", "--accent-amber", "--accent-lime", "--accent-teal"];
  let colors = [];
  let accentColors = [];
  const readColors = () => {
    const style = getComputedStyle(root);
    colors = colorVars
      .map((name) => style.getPropertyValue(name).trim())
      .filter(Boolean);
    if (!colors.length) {
      colors = ["rgba(255,255,255,0.8)"];
    }

    accentColors = accentColorVars
      .map((name) => style.getPropertyValue(name).trim())
      .filter(Boolean);
    if (!accentColors.length) {
      accentColors = colors.slice();
    }
  };

  const canvas = document.createElement("canvas");
  canvas.className = "starfield-canvas";
  canvas.setAttribute("aria-hidden", "true");

  const context = canvas.getContext("2d", { alpha: true });
  if (!context) return;

  let dpr = 1;
  let width = 0;
  let height = 0;
  let stars = [];
  let shootingStar = null;
  let nextShootAt = 0;
  let accentIndex = 0;
  let lastFrameTime = null;
  let rafId = null;

  const createStar = () => {
    let vx = rand(-0.13, 0.13);
    let vy = rand(-0.13, 0.13);
    if (Math.abs(vx) + Math.abs(vy) < 0.06) {
      vx = vx < 0 ? vx - 0.04 : vx + 0.04;
      vy = vy < 0 ? vy - 0.04 : vy + 0.04;
    }

    return {
      x: rand(0, width),
      y: rand(0, height),
      r: rand(0.75, 2.2),
      vx,
      vy,
      twinklePhase: rand(0, Math.PI * 2),
      twinkleSpeed: rand(0.3, 1.2),
      alphaBase: rand(0.55, 0.98),
      color: colors[(Math.random() * colors.length) | 0]
    };
  };

  const createStars = () => {
    const targetCount = Math.min(240, Math.max(95, Math.round((width * height) / 17000)));
    stars = Array.from({ length: targetCount }, createStar);
  };

  const scheduleNextShoot = (nowMs) => {
    nextShootAt = nowMs + rand(3800, 8200);
  };

  const createShootingStar = (nowMs) => {
    const fromLeft = Math.random() < 0.5;
    const speed = rand(950, 1450);
    const x = fromLeft ? -130 : width + 130;
    const y = rand(height * 0.08, height * 0.52);
    const vx = fromLeft ? speed * rand(0.84, 0.96) : -speed * rand(0.84, 0.96);
    const vy = speed * rand(0.16, 0.34);
    const color = accentColors[accentIndex % accentColors.length];

    accentIndex += 1;
    shootingStar = {
      x,
      y,
      vx,
      vy,
      length: rand(90, 170),
      life: 0,
      maxLife: rand(0.85, 1.35),
      color
    };

    scheduleNextShoot(nowMs);
  };

  const updateShootingStar = (deltaSeconds) => {
    if (!shootingStar) {
      return;
    }

    shootingStar.x += shootingStar.vx * deltaSeconds;
    shootingStar.y += shootingStar.vy * deltaSeconds;
    shootingStar.life += deltaSeconds;

    const isExpired = shootingStar.life >= shootingStar.maxLife;
    const isOutOfBounds =
      shootingStar.x < -220 ||
      shootingStar.x > width + 220 ||
      shootingStar.y < -220 ||
      shootingStar.y > height + 220;

    if (isExpired || isOutOfBounds) {
      shootingStar = null;
    }
  };

  const drawShootingStar = () => {
    if (!shootingStar) {
      return;
    }

    const lifeRatio = Math.max(0, Math.min(1, shootingStar.life / shootingStar.maxLife));
    const fade = Math.sin(Math.PI * lifeRatio);
    const speedMag = Math.hypot(shootingStar.vx, shootingStar.vy) || 1;
    const ux = shootingStar.vx / speedMag;
    const uy = shootingStar.vy / speedMag;
    const tailX = shootingStar.x - ux * shootingStar.length;
    const tailY = shootingStar.y - uy * shootingStar.length;

    context.save();
    context.lineCap = "round";
    context.strokeStyle = shootingStar.color;
    context.lineWidth = 2.2;
    context.globalAlpha = 0.78 * fade;
    context.beginPath();
    context.moveTo(shootingStar.x, shootingStar.y);
    context.lineTo(tailX, tailY);
    context.stroke();

    context.globalAlpha = 0.9 * fade;
    context.fillStyle = shootingStar.color;
    context.beginPath();
    context.arc(shootingStar.x, shootingStar.y, 2.2, 0, Math.PI * 2);
    context.fill();
    context.restore();
  };

  const resize = () => {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = Math.max(1, window.innerWidth);
    height = Math.max(1, window.innerHeight);
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    context.setTransform(dpr, 0, 0, dpr, 0, 0);
    createStars();
  };

  const render = (timeMs) => {
    const t = timeMs * 0.001;
    if (lastFrameTime === null) {
      lastFrameTime = timeMs;
    }
    const deltaSeconds = Math.min((timeMs - lastFrameTime) * 0.001, 0.05);
    lastFrameTime = timeMs;

    context.clearRect(0, 0, width, height);

    for (const star of stars) {
      if (!prefersReducedMotion.matches) {
        star.vx += rand(-0.0018, 0.0018);
        star.vy += rand(-0.0018, 0.0018);
        star.vx = Math.max(-0.16, Math.min(0.16, star.vx));
        star.vy = Math.max(-0.16, Math.min(0.16, star.vy));

        star.x += star.vx;
        star.y += star.vy;

        if (star.x < -3) star.x = width + 3;
        if (star.x > width + 3) star.x = -3;
        if (star.y < -3) star.y = height + 3;
        if (star.y > height + 3) star.y = -3;
      }

      const twinkle = 0.75 + 0.25 * Math.sin(t * star.twinkleSpeed + star.twinklePhase);
      context.globalAlpha = star.alphaBase * twinkle;
      context.fillStyle = star.color;
      context.beginPath();
      context.arc(star.x, star.y, star.r, 0, Math.PI * 2);
      context.fill();
    }

    if (!prefersReducedMotion.matches) {
      if (!shootingStar && timeMs >= nextShootAt) {
        createShootingStar(timeMs);
      }
      updateShootingStar(deltaSeconds);
      drawShootingStar();
    }

    context.globalAlpha = 1;
    if (!prefersReducedMotion.matches) {
      rafId = requestAnimationFrame(render);
    }
  };

  const restart = () => {
    if (rafId !== null) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
    readColors();
    resize();
    shootingStar = null;
    lastFrameTime = null;
    scheduleNextShoot(performance.now());
    render(performance.now());
  };

  const init = () => {
    if (document.querySelector(".starfield-canvas")) return;
    document.body.prepend(canvas);
    restart();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }

  window.addEventListener("resize", restart, { passive: true });
  prefersReducedMotion.addEventListener("change", restart);

  const themeObserver = new MutationObserver(() => {
    readColors();
    for (const star of stars) {
      star.color = colors[(Math.random() * colors.length) | 0];
    }
    if (shootingStar) {
      shootingStar.color = accentColors[accentIndex % accentColors.length];
    }
  });
  themeObserver.observe(root, { attributes: true, attributeFilter: ["data-theme"] });
})();
