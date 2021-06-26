from flask.signals import appcontext_popped
import app_logger

from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import load_only

from app import app, db  
from models.data import Posts

class SQL():
    def __init__(self):    
        self.engine = create_engine('sqlite:///test.db')
        self.logger = app_logger.get_logger(__name__)

    def checkDoesExist(self, link):
        try:
            with self.engine.connect() as conn:
                id = conn.execute(f"SELECT count(id) FROM posts WHERE link = '{link}'")
                return id.fetchall()[0][0]
        except Exception as ex:
            self.logger.error(str(ex))

    def addLink(self, link):
        try:
            new_post = Posts(link)
            db.session.add(new_post)
            db.session.commit()
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
