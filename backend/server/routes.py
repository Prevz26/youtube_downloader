#imports 
from server import app
from flask import render_template, request, jsonify, redirect, url_for, flash, session
from pytube import YouTube

@app.route("/", methods = ["GET", "POST"])
@app.route("/api/index/", methods = ["GET", "POST"])
def index():
    return render_template("public/index.html", title = "YOUTUBE DOWNLOADER")
    # redirect(url_for("download"))


@app.route("api/submit/", methods = ["POST"])
def submit():
    if request.method == "POST":
        url = request.form.get('url')
        video = YouTube(url)
        title = video.title
        # data = jsonify(url = url, title = title)
        data ={'url': url, 'title': title}
        return render_template("public/download_page.html", data = data)
    else:
        return redirect(url_for("internal_server_error"))

@app.route("/download/", methods = ["POST"])
def download():
    pass
@app.errorhandler
def page_not_found(error):
    return render_template("error_messages/404.html"), 404
@app.errorhandler
def internal_server_error(error):
    return render_template("error_messages/500.html"), 500

