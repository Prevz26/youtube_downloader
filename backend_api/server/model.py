from server.config import database_config
from server import app
from flask_sqlalchemy import SQLAlchemy
#setting up the database configuration
app.config.update(database_config())

#creating an instance of the flask sqlalchemy and passing the flask application to it
db = SQLAlchemy()
db.init_app(app)


#models
class streams(db.Model):
    pass