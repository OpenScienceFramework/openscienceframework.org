from flask import Flask
import modular

modular.Application.web = Flask(__name__, static_path='/static', static_folder='static')
modular.Application.web.debug = True

###############################################################################
# Register the wiki
###############################################################################

import modular_wiki
import osf_wiki
osf_wiki.app.register(
    'wiki',
    controller=osf_wiki.Wiki(),
    url_bases=['/project/<pid>/', '/project/<pid>/node/<nid>/'],
    template_dirs=["osf_wiki/templates"],
)

###############################################################################
# Register the main page
###############################################################################

app = modular.Application(controller=None)

@app.route('/')
def index(**kwargs):
    return 'home'

app.register(
    'main',
    controller=None,
    url_bases=['/'],
    template_dirs=['.'],
)

###############################################################################

if __name__ == "__main__":
    modular.Application.web.run()
