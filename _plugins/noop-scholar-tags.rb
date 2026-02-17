module Jekyll
  # Compatibility tags so legacy `{% cite %}` / `{% bibliography %}` snippets
  # do not break builds after removing jekyll-scholar.
  class NoopCiteTag < Liquid::Tag
    def render(_context)
      ""
    end
  end

  class NoopBibliographyTag < Liquid::Tag
    def render(_context)
      ""
    end
  end
end

Liquid::Template.register_tag("cite", Jekyll::NoopCiteTag)
Liquid::Template.register_tag("bibliography", Jekyll::NoopBibliographyTag)
