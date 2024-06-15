#imports 
from server import app
from flask import request, jsonify, url_for, session, make_response, redirect
from server.utils import convert_duration, filter_streams, serialize_streams
from server.config import secret_key_config
from secrets import token_hex
from pytube import YouTube

#setting the secret key
secret_key_config(token_hex(16))

#error handlers
@app.errorhandler(404)
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

@app.errorhandler(500)
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


#routes
@app.route("/api/video/info/", methods = ["GET", "POST"])
def video_info():
    """
    Retrieves information about a YouTube video.

    This function handles both GET and POST requests to the "/api/video/info/" endpoint.
    If the request method is POST, it retrieves the JSON data from the request body and stores it in the session under the key "url".
    It then extracts the URL from the JSON data and attempts to create a YouTube object using the pytube library.
    If successful, it retrieves various attributes of the video object, such as the author, title, video ID, thumbnail URL, channel URL, and duration.
    It constructs a dictionary with these attributes and returns it as a JSON response.
    If an exception occurs during the process, it returns a JSON response with an "error" key containing the string representation of the exception.

    Returns:
        A JSON response containing the video information if successful, or a JSON response with an "error" key if an exception occurs.

    Raises:
        None.
    """


    if request.method == "POST":
        video = request.get_json()
        session["url"] = video
        url = video.get("url")
        try:
            video_object = YouTube(url)
            author = video_object.author,
            title = video_object.title
            video_id = video_object.video_id
            tumbnail = video_object.thumbnail_url
            channel_url = video_object.channel_url
            duration = convert_duration(video_object.length)
            #more attributes added later
            data = {"video_url": url,
                "author":author,
                "title": title, 
                "tumbnail":tumbnail, 
                "channel_url": channel_url,
                "video_id": video_id, 
                 "duration": f"{duration} min"
                        }
            return jsonify(data)
        except Exception as e:
                return jsonify({"error": str(e)}), 500


@app.route("/api/streams/", methods = ["GET"])
def streams():
    if "url" in session.keys():
        try:
            url = session["url"]
            url = url.get('url')

            video_object = YouTube(url)
            filtered_streams = filter_streams(video_object.streams, progressive=True)
            stream = serialize_streams(filtered_streams)
            session["streams"] = stream
            return session["streams"]
        except Exception as e:
                return jsonify({"error":str()})



# class download(Resource):
#     def get(self):
#         return session["streams"]
    
# api.add_resource(download, "/download/")

# # @app.route("/download/", methods = ["GET", "POST"])  
# # def download():
# #     if session["streams"]:
# #         streams:list[dict] = session["streams"]
# #         return streams
# #         for stream in streams:
#             # return stream


