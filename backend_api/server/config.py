from server import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


def secret_key_config(secret_key:str) -> None:
    """
    Set the secret key for the Flask application.

    Parameters:
        secret_key (str): The secret key for the application to be set.

    Returns:
        None
    """

    app.config['SECRET_KEY'] = secret_key


def database_config() -> dict:
    """
    Returns a dictionary containing the configuration settings for the database.

    :return: A dictionary with the following keys:
             - "SQLALCHEMY_DATABASE_URI": The URI for the database connection.
             - "SQLALCHEMY_TRACK_MODIFICATIONS": A boolean indicating whether or not to track modifications to database objects.
    :rtype: dict
    """
    return {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///student.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
