#!/usr/bin/env python3


# +
# import(s)
# -
from dotenv import dotenv_values
from pathlib import Path
from pyindi.webclient import INDIWebApp
from pyindi.webclient import INDIHandler
from tornado.web import StaticFileHandler

import os


# +
# config_dict
# -
CURRENT_DIR = os.path.dirname(os.path.abspath(os.path.expanduser(os.path.realpath(__file__))))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
CONFIG_FILE = f"{PARENT_DIR}/.env"
config_dict = dotenv_values(CONFIG_FILE)

DEVICES = ["*"]
INDIHOST = config_dict["INDIHOST"]
INDIPORT = int(config_dict["INDIPORT"])
TEMPLATE = f"{CURRENT_DIR}/ninety-prime.html"
WEBHOST = config_dict["WEBHOST"]
WEBPORT = int(config_dict["WEBPORT"])


# +
# Build handlers with path for rendering, each path should have a handler
#  and pass additional variables to appear in the html template
# -
class GUI(INDIHandler):
    def get(self):
        self.indi_render(TEMPLATE, devices=DEVICES)


# +
# start
# -
web_app = INDIWebApp(webport=WEBPORT, indihost=INDIHOST, indiport=INDIPORT)
print(f"Go to http://{WEBHOST}:{WEBPORT}")
print(f"Alternate http://{WEBHOST}:{WEBPORT}/indi")


# Attach handlers and build the application
# For images, use tornado.web.StaticFileHandler and link the path
web_app.build_app(
    [
        (r"/", GUI)
    ],
)
