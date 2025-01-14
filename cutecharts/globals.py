import os

from jinja2 import Environment, FileSystemLoader


class _NotebookType:
    JUPYTER_NOTEBOOK = "jupyter_notebook"
    JUPYTER_LAB = "jupyter_lab"
    # NTERACT = "nteract"
    # ZEPPELIN = "zeppelin"


class _AssetsHost:
    DEFAULT_HOST = "https://cdn.jsdelivr.net/npm/chart.xkcd@1.1/dist/"


NotebookType = _NotebookType()
AssetsHost = _AssetsHost()


_ASSETS_DEPS_MAP = {"chartXkcd": "chart.xkcd.min"}


class _CurrentConfig:
    ASSETS_HOST = AssetsHost.DEFAULT_HOST
    ASSETS_DEPS_MAP = _ASSETS_DEPS_MAP
    NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    GLOBAL_ENV = Environment(
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        loader=FileSystemLoader(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "render", "templates"
            )
        ),
    )


CurrentConfig = _CurrentConfig()
