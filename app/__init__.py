from flask import Flask
from flask_minify import minify

app = Flask(__name__)
minify(app=app,html=True,js=False,cssless=False)

from app import routes