from django import template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<div class="code-block"><pre><code>%s</code></pre></div>\n' % \
                   mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        code_html = highlight(code, lexer, formatter)
        return """
            <div class="code-block">
                <button class='code-theme-toggle' onclick='toggleCodeTheme()'>
                    <i class="toggle-icon fas fa-sun"></i>
                </button>
                {}
            </div> 
        """.format(code_html)
        # return "<div class='code-block'>" + code_html + "</div>"


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(value)
