from __future__ import annotations
import importlib.metadata

with open("../requirements.txt") as f:
    skshapes_version = f.readline().replace(" ", "")

install_command = f"pip install {skshapes_version}"
rst_epilog = f".. |install_command| replace:: {install_command}"

templates_path = ["templates"]

# -- pyvista configuration ---------------------------------------------------
# See: https://github.com/pyvista/pyvista/blob/main/doc/source/conf.py
import pyvista
import os
from pyvista.core.errors import PyVistaDeprecationWarning
from pyvista.core.utilities.docs import linkcode_resolve, pv_html_page_context  # noqa: F401
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper as Scraper

# Manage errors
pyvista.set_error_output_file("errors.txt")
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True  # Not necessary - simply an insurance policy
# Preferred plotting style for documentation
pyvista.set_plot_theme("document")
pyvista.global_theme.window_size = [1024, 768]
pyvista.global_theme.font.size = 22
pyvista.global_theme.font.label_size = 22
pyvista.global_theme.font.title_size = 22
pyvista.global_theme.return_cpos = False
pyvista.set_jupyter_backend(None)
# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath("./images/"), "auto-generated/")
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True
os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'

class ResetPyVista:
    """Reset pyvista module to default settings."""

    def __call__(self, gallery_conf, fname):
        """Reset pyvista module to default settings

        If default documentation settings are modified in any example, reset here.
        """
        import pyvista

        pyvista._wrappers['vtkPolyData'] = pyvista.PolyData
        pyvista.set_plot_theme('document')

    def __repr__(self):
        return 'ResetPyVista'


reset_pyvista = ResetPyVista()


project = "Scikit Shapes tutorial"
copyright = "2024, Louis Pujol"
author = "Louis Pujol"
version = release = ""
html_title = "Scikit-shapes tutorial"

extensions = [
    # 'sphinx_tabs.tabs',
    "sphinx_design",
    # "myst_parser",
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    # "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    # "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    'sphinx_gallery.gen_gallery',
]

source_suffix = [".rst"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

sphinx_tabs_valid_builders = ['linkcheck']

html_theme = "furo"

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Louis-Pujol/scikit-shapes-tutorial",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

myst_enable_extensions = [
    "colon_fence",
]

from sphinx_gallery.sorting import FileNameSortKey

sphinx_gallery_conf = {
    'examples_dirs': '../examples/',   # path to your example scripts
    'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
    "doc_module": "pyvista",
    "image_scrapers": (Scraper(), "matplotlib"),
    "first_notebook_cell": "%matplotlib inline",
    "reset_modules": (reset_pyvista,),
    "reset_modules_order": "both",
    "within_subsection_order": FileNameSortKey,
}
