import os
import yaml
master_doc = 'index'
html_theme = 'redirect_template'
html_theme_path = ['.']

try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'redirect.yml')) as redirect:
        redirect_data = redirect.read()
        redirect_data = yaml.safe_load(redirect_data)
except:
    pass


html_context = redirect_data