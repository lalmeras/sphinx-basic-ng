"""A modern skeleton for Sphinx themes."""

__version__ = "0.0.1.dev7"

from pathlib import Path
from typing import Any, Dict

import sphinx.application

_THEME_PATH = (Path(__file__).parent / "theme" / "basic-ng").resolve()


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    from ._navigation import setup_navigation

    app.require_sphinx("3.0")
    app.add_html_theme("basic-ng", str(_THEME_PATH))

    setup_navigation(app)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
