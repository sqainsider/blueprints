# project/__int__.py

from flask import flask
from flask.ext.sqlalchemy import SQLALchemy

app= Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLALchemy(app)

from project.users.views import users_blueprint
from project.tasks.views import tasks_blueprint

#register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)
