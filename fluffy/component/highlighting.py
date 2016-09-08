import pygments
import pygments.lexers
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

from fluffy.app import app


# We purposefully don't list all possible languages, and instead just the ones
# we think people are most likely to use.
UI_LANGUAGES_MAP = {
    'bash': 'Bash / Shell',
    'c': 'C',
    'c++': 'C++',
    'cheetah': 'Cheetah',
    'diff': 'Diff',
    'groovy': 'Groovy',
    'html': 'HTML',
    'java': 'Java',
    'javascript': 'JavaScript',
    'json': 'JSON',
    'makefile': 'Makefile',
    'objective-c': 'Objective-C',
    'php': 'PHP',
    'python3': 'Python',
    'ruby': 'Ruby',
    'scala': 'Scala',
    'sql': 'SQL',
    'yaml': 'YAML',
}


_pygments_formatter = HtmlFormatter(
    noclasses=True,
    linespans='line',
    nobackground=True,
    style=get_style_by_name('xcode'),
)


def guess_lexer(text, language, opts=None):
    lexer_opts = {'stripnl': False}
    if opts:
        lexer_opts = dict(lexer_opts, **opts)

    try:
        return pygments.lexers.get_lexer_by_name(language, **lexer_opts)
    except pygments.util.ClassNotFound:
        try:
            return pygments.lexers.guess_lexer(text, **lexer_opts)
        except pygments.util.ClassNotFound:
            return pygments.lexers.get_lexer_by_name('python', **lexer_opts)


@app.template_filter()
def highlight(text, lexer):
    return pygments.highlight(
        text,
        lexer,
        _pygments_formatter,
    )
