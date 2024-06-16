#imports 
from flask import request, jsonify, url_for, session, make_response, redirect, Blueprint
from server.utils import convert_duration, filter_streams, serialize_streams
from server.config import secret_key_config
from secrets import token_hex
from pytube import YouTube
import json

#setting the secret key
secret_key_config(token_hex(16))

main = Blueprint("main", __name__)

#routes
@main.route("/", methods = ["GET","POST"])
@main.route("/api/video_info/", methods = ["GET","POST"])
def video_info():
    """
    Retrieves information about a YouTube video.

    This function handles both the POST requests to the "/api/video/info/" endpoint.
    If the request method is POST, it retrieves the JSON data from the request body and stores it in the session under the key "url".
    It then extracts the URL from the JSON data and attempts to create a YouTube object using the pytube library.
    If successful, it retrieves various attributes of the video object, such as the author, title, video ID, thumbnail URL, channel URL, and duration.
    It constructs a dictionary with these attributes and returns it as a JSON response.
    If an exception occurs during the process, it returns a JSON response with an "error" key containing the string representation of the exception.

    Returns:
        A JSON response 
        containing the video information if successful, or a JSON response with an "error" key if an exception occurs.

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


@main.route("/api/streams/", methods = ["GET"])
def streams():
    """
    Retrieves the streams of a YouTube video.

    This function handles GET requests to the "/api/streams/" endpoint.
    It checks if the "url" key exists in the session dictionary.
    If it exists, it retrieves the URL from the session dictionary and attempts to create a YouTube object using the pytube library.
    It then filters the video streams based on the progressive attribute and serializes them.
    The serialized streams are stored in the session dictionary under the key "streams".
    Finally, it returns the serialized streams from the session dictionary.

    Returns:
        The serialized streams from the session dictionary if successful.
        A JSON response with an "error" key if an exception occurs.
    """
    try:
        if "url" in session.keys():
            url = session["url"]
            if url is None or 'url' not in url:
                raise TypeError("URL is not provided or malformed.")
            else:
                    url = url.get('url')
                    try:
                        video_object = YouTube(str(url))
                        filtered_streams = filter_streams(video_object.streams, progressive=True)
                        stream = serialize_streams(filtered_streams)
                        session["streams"] = stream
                        return jsonify(session["streams"])
                    except Exception as e:
                            return jsonify({"error":str("error")})
        else:
            raise TypeError("URL already in session.")
    except TypeError:
        return jsonify({"error":f"post the url to {url_for('video_info')} endpoint"}), 500

@main.route("/api/download/", methods = ["GET", "POST"])  
def download():
    try:
        if session["streams"]:
            return (session["streams"])
    except KeyError:
        return jsonify({"message": "no stream found"})
    else:
        return jsonify({"message": "no stream found"})
        streams:list[dict] = session["streams"]
        return streams


