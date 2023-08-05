#############################################################################
# Copyright (c) 2018, Voila Contributors                                    #
#                                                                           #
# Distributed under the terms of the BSD 3-Clause License.                  #
#                                                                           #
# The full license is in the file LICENSE, distributed with this software.  #
#############################################################################

import os
import gettext

import tornado.web
from jinja2 import Environment, FileSystemLoader

from jupyter_server.utils import url_path_join
from jupyter_server.base.handlers import path_regex
from jupyter_server.base.handlers import FileFindHandler

from .paths import ROOT, TEMPLATE_ROOT, STATIC_ROOT
from .handler import VoilaHandler
from .treehandler import VoilaTreeHandler

def load_jupyter_server_extension(server_app):
    web_app = server_app.web_app

    jenv_opt = {"autoescape": True}
    env = Environment(loader=FileSystemLoader(TEMPLATE_ROOT), extensions=['jinja2.ext.i18n'], **jenv_opt)
    web_app.settings['voila_jinja2_env'] = env

    nbui = gettext.translation('nbui', localedir=os.path.join(ROOT, 'i18n'), fallback=True)
    env.install_gettext_translations(nbui, newstyle=False)

    host_pattern = '.*$'
    base_url = url_path_join(web_app.settings['base_url'])
    web_app.add_handlers(host_pattern, [
        (url_path_join(base_url, '/voila/render' + path_regex), VoilaHandler, {
            'config': server_app.config
        }),
        (url_path_join(base_url, '/voila'), VoilaTreeHandler),
        (url_path_join(base_url, '/voila/tree' + path_regex), VoilaTreeHandler),
        (url_path_join(base_url, '/voila/static/(.*)'),  tornado.web.StaticFileHandler, {'path': STATIC_ROOT}),
        # this handler serves the nbextensions similar to the classical notebook
        (
            url_path_join(base_url, r'/voila/nbextensions/(.*)'),
            FileFindHandler,
            {
                'path': web_app.settings['nbextensions_path'],
                'no_cache_paths': ['/'],  # don't cache anything in nbextensions
            },
        )
    ])
