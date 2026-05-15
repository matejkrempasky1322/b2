# -*- coding: utf-8 -*-
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

togglebutton_hint = "Zobraziť kód"
togglebutton_hint_hide = "Skryť kód"
default_dark_mode = True
language = 'sk'
exclude_patterns = ['_build', '**.ipynb_checkpoints']
html_theme = 'sphinx_rtd_theme'
html_static_path = []
nbsphinx_allow_errors = True

nbsphinx_prolog = """
.. raw:: html

    <script>
    window.addEventListener('load', function() {
        var inputs = document.querySelectorAll('.nbinput');
        inputs.forEach(function(el) {
            var btn = document.createElement('button');
            btn.textContent = 'Zobraziť kód';
            btn.className = 'toggle-btn';
            btn.style.cssText = 'background:#2980b9;color:white;border:none;padding:4px 10px;border-radius:3px;cursor:pointer;margin:4px 0;';
            var content = el.querySelector('.input_area');
            if(content) {
                content.style.display = 'none';
                btn.addEventListener('click', function() {
                    content.style.display = content.style.display === 'none' ? '' : 'none';
                    btn.textContent = content.style.display === 'none' ? 'Zobraziť kód' : 'Skryť kód';
                });
                el.insertBefore(btn, content);
            }
        });
    });
    </script>
"""