import os

from flask import (
    current_app,
    render_template,
    url_for,
    abort,
)
from flask import request, redirect
from jinja2.exceptions import TemplateNotFound

from app.main import main
from app.utils import convert_and_save
from app.utils import not_exist

main.register_error_handler(TemplateNotFound, not_exist)
main.register_error_handler(404, not_exist)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return redirect(url_for(".index"))
    file = request.files.get("file")
    if not file or not convert_and_save(file, file.filename):
        abort(400)
    return redirect(url_for(".blog", values=format(file.filename.split(".")[0])))


@main.route("/blog/<string:blog_name>")
def blog(blog_name):
    return render_template("blog/{}.html".format(blog_name))


@main.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(current_app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
