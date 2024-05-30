#imports 
from server import app
from flask import render_template, request, jsonify, redirect, url_for, flash, session
from pytube import YouTube

@app.route("/", methods = ["GET", "POST"])
@app.route("/index/", methods = ["GET", "POST"])
def index():
    """
    This function is a route handler for the root and index routes. It handles both GET and POST requests.
    It renders the "public/index.html" template with the title "YOUTUBE DOWNLOADER" for visibilty purpose the frontend will handle this.
    #the index.html is a form that collects the url for the youtube video and sends it to the submit route, but frontend will redesign and just send the url to the /submit endpoint.  

    Parameters:
    None

    Returns:
    A rendered template of "public/index.html" with the title "YOUTUBE DOWNLOADER".
    """
    return render_template("public/index.html")


@app.route("/video/info/", methods = ["GET", "POST"])
@app.route("/video/<link>/", methods = ["GET", "POST"])
def submit(link):
    """
    This function is a route handler for the "/submit/" route. It handles both GET and POST requests.
    
    Parameters:
    None
    
    Returns:
    - If the request method is POST:
        - If the URL is successfully fetched and parsed:
            - Returns a JSON response containing the information of the YouTube video.
        - If the URL is not provided or cannot be fetched:
            - Returns a redirect to the "internal_server_error" route.
    - If the request method is GET:
        - Returns a redirect to the "internal_server_error" route.
    """
    aa = YouTube(link)
    print(aa.title)
    
    if request.method == "POST":
        url = request.form.get('url')
        video = YouTube(url)
        title = video.title
        video_id = video.video_id
        tumbnail = video.thumbnail_url
        channel_url = video.channel_url

        #more attributes added later
        data = {"video_url": url,
                "author": video.author,
                 "title": title, 
                 "tumbnail":tumbnail, 
                 "channel_url": channel_url,
                 "video_id": video_id, 
                 "duration": video.length
                }
        #https://img.youtube.com/vi/pj1iLRljwxI/default.jpg
        return jsonify(data)
    else:
        return redirect(url_for("internal_server_error"))

def generate_tumbnail(id:str):
    return 
@app.route("/download/", methods = ["POST"])

def download():
    pass

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Page not found"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(error="Something went wrong"), 500

