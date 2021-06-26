from urllib import parse
from flask import request, json, render_template
from app import app
import app_logger

from models.data import Posts
from script import Parser

logger = app_logger.get_logger(__name__)
parser = Parser()

@app.route("/create_post", methods=['GET', 'POST'])
def create_post():
    try:
        parser.parsePost()
        return 'home'
    except Exception as ex:
        logger.error(str(ex))