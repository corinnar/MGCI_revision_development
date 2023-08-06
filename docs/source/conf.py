# Configuration file for the Sphinx documentation builder.

from datetime import datetime

# -- Project information

project = "SDG 15.4.2: (a) Mountain Green Cover Index and (b) proportion of degraded mountain land"
copyright = f"2023 - FAO SEPAL - UNEP-WCMC"
author = 'FAO SEPAL - UNEP-WCMC'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

--file-insertion-enabled

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
