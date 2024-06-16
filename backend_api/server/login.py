from flask import Blueprint, request, jsonify, session
from flask_login import login_user, logout_user, login_required
from .model import User
from .config import secret_key_config
from secrets import token_hex

#setting blueprint
login = Blueprint("login", __name__)

#setting the secret key
secret_key_config(token_hex(16))