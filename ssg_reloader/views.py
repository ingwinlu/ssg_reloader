from ssg_reloader import app
from flask import jsonify, redirect
from urllib import url2pathname
import os

from utils import inject_js

@app.route("/_ssg_reloader")
def ssg_reload():
    return jsonify(reload=app._watchdog.next())

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def serve(path):
    if path.endswith("/"):
        path = path + "index.html"
    path = url2pathname(path)
    if path.endswith("html"):
        file_path = os.path.join(app._static_folder, path)
        #this will be terrible slow
        return inject_js(html_path=file_path, timeout=app._inject_timeout)
    else:
        return app.send_static_file(path)
    return redirect("/", code=302)

