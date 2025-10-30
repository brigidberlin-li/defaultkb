# Configuration file for the Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Help Yahoo Default KB'
copyright = '2025'
author = 'Mary Beyt'

release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
