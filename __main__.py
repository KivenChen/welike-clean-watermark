import flask import Flask
from flask import request, url_for
from proc import *
app = Flask(__name__)

@app.route('dispatch/weizuotu-watermark')
def fix():
    file = request.files[request.args['filename']]
    result = modify('weizuotu', Image.open(file))
    return url_for('result')

app.run()