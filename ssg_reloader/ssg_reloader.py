from flask import Flask, jsonify, redirect

import utils

app = Flask(__name__)

@app.route("/_ssg_reloader")
def ssg_reload():
    return jsonify(reload=watchdog.next())

@app.route("/", defaults={"path": "/"})
@app.route("/<path:path>")
def serve(path):
    if path.endswith("/"):
        path = path + "index.html"
    if path.endswith("html"):
        #this will be terrible slow
        return utils.inject_js(args.root_directory + path)
    else:
        return app.send_static_file(path)
    return redirect("/", code=302)

if __name__ == '__main__':
    args = utils.get_args()
    watchdog = utils.watchdog_generator(args.root_directory)
    watchdog.next() #remove first positive
    
    app._static_folder = args.root_directory
    
    app.run(
        debug = args.debug,
        host  = args.ip,
        port  = args.port)

