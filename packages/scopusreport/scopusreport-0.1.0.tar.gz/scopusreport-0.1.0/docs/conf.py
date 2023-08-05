#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.join(os.path.abspath(os.pardir)))
autodoc_mock_imports = ["_tkinter"]

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.insert(0, project_root)

import scopusreport

# General configuration
needs_sphinx = '1.3'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'scopusreport'
author = 'John Kitchin and Michael E. Rose'
copyright = ','.join(['2019', author])

version = scopusreport.__version__
release = scopusreport.__version__

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'
todo_include_todos = False
autodoc_member_order = 'groupwise'

# Options for HTML output
html_theme = 'alabaster'
html_theme_options = {
    'github_user': 'scopus-api',
    'github_repo': 'scopus-report',
    'github_banner': 'true',
    'github_button': 'true',
    'github_type': 'star',
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

html_static_path = ['_static']

# Options for HTMLHelp output
html_show_sourcelink = True
htmlhelp_basename = 'scopusreportdoc'
autoclass_content = 'both'

# Option to group members of classes
autodoc_member_order = 'groupwise'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'scopusreport.tex', 'scopusreport Documentation',
     author, 'manual'),
]

# Options for manual page output
man_pages = [
    (master_doc, 'scopusreport', 'scopusreport Documentation',
     [author], 1)
]

# Options for Texinfo output
texinfo_documents = [
    (master_doc, 'scopusreport', 'scopusreport Documentation',
     author, 'scopusreport', 'One line description of project.',
     'Miscellaneous'),
]
