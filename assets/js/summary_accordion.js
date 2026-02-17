(() => {
  const initSummaryAccordions = () => {
    const getScrollOffset = () => {
      const navbar = document.querySelector(".navbar");
      let offset = 12;

      if (!navbar) {
        return offset;
      }

      const navbarStyles = window.getComputedStyle(navbar);
      if (navbarStyles.position === "fixed" || navbarStyles.position === "sticky") {
        offset += navbar.getBoundingClientRect().height;
      }

      return offset;
    };

    const focusAndScrollToPanel = (panel) => {
      const summary = panel.querySelector("summary.summary-panel-summary");
      if (summary) {
        summary.focus({ preventScroll: true });
      }

      const panelTop = panel.getBoundingClientRect().top + window.scrollY - getScrollOffset();
      window.scrollTo({
        top: Math.max(panelTop, 0),
        behavior: "smooth",
      });
    };

    const grids = document.querySelectorAll(".summary-panel-grid");

    grids.forEach((grid) => {
      const getPanels = () => Array.from(grid.querySelectorAll("details.summary-panel-expandable"));
      const panels = getPanels();

      if (!panels.length) {
        return;
      }

      panels.forEach((panel, index) => {
        panel.dataset.summaryAccordionIndex = String(index);
      });

      const reorderPanels = (openPanel = null) => {
        const orderedPanels = getPanels().sort((a, b) => {
          if (openPanel) {
            if (a === openPanel) {
              return -1;
            }
            if (b === openPanel) {
              return 1;
            }
          }

          return Number(a.dataset.summaryAccordionIndex) - Number(b.dataset.summaryAccordionIndex);
        });

        orderedPanels.forEach((panel) => {
          grid.appendChild(panel);
        });
      };

      panels.forEach((panel) => {
        panel.addEventListener("toggle", () => {
          const currentPanels = getPanels();

          if (!panel.open) {
            const currentlyOpenPanel = currentPanels.find((candidate) => candidate.open) || null;
            reorderPanels(currentlyOpenPanel);
            return;
          }

          currentPanels.forEach((otherPanel) => {
            if (otherPanel !== panel && otherPanel.open) {
              otherPanel.open = false;
            }
          });

          reorderPanels(panel);
          requestAnimationFrame(() => {
            focusAndScrollToPanel(panel);
          });
        });
      });

      const initiallyOpenPanel = panels.find((panel) => panel.open) || null;
      reorderPanels(initiallyOpenPanel);
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initSummaryAccordions);
  } else {
    initSummaryAccordions();
  }
})();
