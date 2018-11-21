from flask import Flask
from flask_minify import minify

app = Flask(__name__)
minify(app=app)

from app import routes