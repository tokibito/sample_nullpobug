# coding: utf-8
from __future__ import print_function
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * (1024 ** 3)
# app.config["DEBUG"] = True


def custom_stream_factory(self, total_content_length, filename, content_type,
                          content_length=None):
    """添付ファイルの書き込みストリーム生成
    """
    return open("/vagrant/output.dat", "wb")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    print("uploaded start: ", datetime.now())
    # filesに触る前に差し替え
    request._get_file_stream = custom_stream_factory
    upload_file = request.files["upload_file"]
    print("get upload_file: ", datetime.now())
    filesize = os.fstat(upload_file.stream.fileno()).st_size
    upload_file.stream.close()
    print("close: ", datetime.now())
    print("uploaded finish: ", datetime.now())
    files = [{
        "name": upload_file.filename,
        "size": filesize,
    }]
    return jsonify({
        "message": u"アップロード完了({} bytes)".format(filesize),
        "files": files})


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)
