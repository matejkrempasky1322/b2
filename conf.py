project = 'Interaktívna učebnica fyziky'
copyright = '2026, Matej Krempaský'
author = 'Matej Krempaský'
release = '1.0'

extensions = [
    'nbsphinx',
    'sphinx_togglebutton',
    'sphinx_rtd_dark_mode',
    'sphinx_copybutton',
    'sphinx_design',
]

default_dark_mode = False
language = 'sk'
exclude_patterns = ['_build', '**.ipynb_checkpoints']

html_theme = 'sphinx_rtd_theme'
html_static_path = []