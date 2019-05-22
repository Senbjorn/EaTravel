from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)
CORS(app)

from back import routes