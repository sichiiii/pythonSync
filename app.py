from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)

if __name__ == "__main__":
    
    from routes import *

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)
    app.run(debug=True, host='0.0.0.0')

