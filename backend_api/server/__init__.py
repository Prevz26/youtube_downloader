from flask import Flask

app = Flask(__name__)

from server import routes, model, config, utils
# from utils import utility