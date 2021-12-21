from flask import Flask
from flask_cors import CORS
from api.configs import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)

from api.modules.misc import mod as miscMod
from api.modules.customer import mod as customerMod
from api.modules.accounts import mod as accountMod

app.register_blueprint(miscMod)
app.register_blueprint(customerMod)
app.register_blueprint(accountMod)
