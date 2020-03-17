import os
from flask import Flask, request, render_template
import requests
import urllib3.request

app = Flask(__name__)

url = "http://localhost:5000/api/classification/classify"


@app.route('/handle_form', methods=['POST'])
def handle_form():
    print("Posted file: {}".format(request.files['file']))
    file = request.files['file']
    files = {'file': file.read()}
    r = requests.post("http://localhost:5000/api/classification/classify", files=files)
    return r.text

@app.route("/")
def index():
    return render_template("upload.html");   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)