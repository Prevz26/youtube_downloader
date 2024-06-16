from flask import Flask

app = Flask(__name__)

from server import routes, model, config, utils, login, error_handling
# from utils import utility