from flask import Blueprint

from webapi.libs.config import Config
from webapi.libs.log import Logger

description: str = "It's an example plugin"

bp: Blueprint = None
name: str = None
logger: Logger = None
config: Config = None
macros: dict = {}
provides_pages: list = [
    ('Template', 'dashboard')
]
request_macros = ['config', 'logger']


def set_blueprint(blueprint: Blueprint):
    global bp
    bp = blueprint

    from . import routes


def post_loading_actions():
    logger.debug("No post loading action defined in plugintemplate.")
