#!/usr/bin/python3.8
from pathlib import Path
from dotenv import dotenv_values

from tornado.web import StaticFileHandler
from pyindi.webclient import INDIWebApp, INDIHandler

# Load configuration
CURRENT_DIR = Path(__file__).parent  # The current directory
config = dotenv_values(CURRENT_DIR.parent / ".env")

# Configuration
WEBPORT = int(config["WEBPORT"])  # The port for the web app
INDIPORT = int(config["INDIPORT"])  # The indiserver port
INDIHOST = config["INDIHOST"]  # Where the indiserver is running
DEVICES = ["*"]  # All devices is called by an asterisk

TEMPLATE = CURRENT_DIR / "ninety-prime.html"
RESOURCES_PATH = CURRENT_DIR / "resources"


# Build handlers with path for rendering, each path should have a handler
class GUI(INDIHandler):
    def get(self):
        # Pass additional variables to appear in the html template
        self.indi_render(TEMPLATE, devices=DEVICES)


web_app = INDIWebApp(webport=WEBPORT, indihost=INDIHOST, indiport=INDIPORT)

print(f"Go to http://<server_name>:{WEBPORT}")
print("If the server is on localhost go to:")
print(f"http://localhost:{WEBPORT}/")

# Attach handlers and build the application
# For images, use tornado.web.StaticFileHandler and link the path
web_app.build_app(
    [
        (r"/", GUI),
        (r"/resources/(.*)", StaticFileHandler, {"path": RESOURCES_PATH})
    ],
)
