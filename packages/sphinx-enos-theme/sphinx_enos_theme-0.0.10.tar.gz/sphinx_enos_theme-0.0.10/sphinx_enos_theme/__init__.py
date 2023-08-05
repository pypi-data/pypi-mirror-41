"""Sphinx ENOS theme.

From https://github.com/TRoam/sphinx-enos-theme.

"""
from os import path

__version__ = '0.0.10'
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir

# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('sphinx_enos_theme', path.abspath(path.dirname(__file__)))
