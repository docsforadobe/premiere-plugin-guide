# -*- coding: utf-8 -*-

import sys
import os
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

def setup(app):
    try:
      app.add_stylesheet('extra.css')

    except:
      app.add_css_file('extra.css')

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

extensions = ['sphinx_rtd_dark_mode']

default_dark_mode = False

# General information about the project.
project = u'Premiere Pro C++ SDK Guide'
copyright = u'1992–2020 Adobe Systems Incorporated'
author = u'Adobe Systems Incorporated'

version = u'24.0.0'
release = u'24.0'

pygments_style = 'sphinx'

highlight_language = "c++"

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'ppro-sdk-guide'
