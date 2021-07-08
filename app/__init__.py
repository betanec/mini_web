from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_script import Manager
application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
 
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# if __name__ == "__main__":
#     manager.run()
#     db.create_all()
from app import routes, models