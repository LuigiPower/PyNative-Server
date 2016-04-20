import json
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
from flask.ext.triangle import Triangle

class PyNative():

    def __init__(self):
        self.flask = Flask(__name__, static_path="/static")
        Triangle(self.flask)

    def getRequestData(self, value):
        return request.args.get(value)

    def getHeader(self, value):
        return request.headers.get(value)

    def getImage(self, filename, imgType):
        realpath = os.path.abspath(filename)
        if imgType == "svg":
            imgType = imgType + "+xml"
        return send_file(realpath, mimetype='image/' + imgType)

    def render(self, screen):
        mimetype = self.getHeader('Content-Type')

        result = "unknown"
        if mimetype == "application/json":
            result = screen.get_json()
        else:
            json = screen.get_json()
            result = render_template("index.html", data = json, pagetitle = screen.data['title'])
        return result
