from django import template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        print(lang)
        formatted_code = ""
        if not lang:
            lang = "bash"
            # formatted_code = "<div class='highlight'>" + mistune.escape(code) + "</div>"
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        formatted_code = highlight(code, lexer, formatter)
        return """
            <div class="code-block dark">
                <button class='code-theme-toggle' onclick='toggleCodeTheme()'>
                    <i class="toggle-icon fas fa-sun"></i>
                </button>
                {}
            </div> 
        """.format(formatted_code)


class PreviewRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        formatted_code = ""
        if not lang:
            lang = "code"
            # formatted_code = "<div class='highlight'>" + mistune.escape(code) + "</div>"
        return """
            &lt;{} removed for preview/>
        """.format(lang)


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(value)

@register.filter
def preview(value):
    render = PreviewRenderer()
    markdown = mistune.Markdown(renderer=render)
    return markdown(value)
