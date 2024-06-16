from flask import Blueprint, jsonify, make_response

error_handler = Blueprint("error_handler", __name__)

# error handlers
@error_handler.errorhandler(404)
def not_found(error):
    """
        Handles the case when a 404 error occurs.

        This function is an error handler for the Flask application. It is registered as an error handler for the 404 error code. When a 404 error occurs, this function is called to handle the error.

        Parameters:
            error (Exception): The exception object representing the 404 error.

        Returns:
            Response: A Flask response object with a JSON payload containing an "error" key set to the string "Not found". The response has a status code of 404.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)

@error_handler.errorhandler(500)
def server_error(error):
    """
    Error handler for 500 Internal Server Error.

    This function is registered as an error handler for the Flask application. It is called when a 500 error occurs. It creates a Flask response object with a JSON payload containing an "error" key set to the string "server error". The response has a status code of 500.

    Parameters:
        error (Exception): The exception object representing the 500 error.

    Returns:
        Response: A Flask response object with a JSON payload and a status code of 500.
    """

    return make_response(jsonify({'error': 'server error'}), 500)

@error_handler.errorhandler(405)
def method_not_allowed(error):
    """
    Handles the case when a 405 error occurs.

    This function is an error handler for the Flask application. It is registered as an error handler for the 405 error code. When a 405 error occurs, this function is called to handle the error.

    Parameters:
        error (Exception): The exception object representing the 405 error.

    Returns:
        Response: A Flask response object with a JSON payload containing an "error" key set to the string "Method not allowed". The response has a status code of 405.
    """
    return make_response(jsonify({'error': 'Method not allowed'}), 405)