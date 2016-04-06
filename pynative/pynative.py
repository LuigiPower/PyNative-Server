import json
from flask import Flask
from flask import request
from flask import render_template
from flask.ext.triangle import Triangle

class PyNative():

    def __init__(self):
        self.flask = Flask(__name__, static_path="/static")
        Triangle(self.flask)

    def getRequestData(self, value):
        return request.args.get(value)

    def getHeader(self, value):
        return request.headers.get(value)

class ElementBuilder():

    json = {}

    def __init__(self, jsoninit):
        self.json = jsoninit

    @classmethod
    def createTextView(cls, el_id, text):
        json = {
                "type": "textview",
                "id": el_id,
                "text": text
            }

        return cls(json)

    @classmethod
    def createGotoButton(cls, el_id, text, toScreen):
        json = {
                "type": "button",
                "id": el_id,
                "text": text,
                "action": {
                    "type": "goto",
                    "screen": toScreen
                    }
                }

        return cls(json)

    def getAsDict(self):
        return self.json


class ViewBuilder():

    element_list = []

    def __init__(self, context, view_screenname = "MainScreen", view_title = "PyNative!"):
        self.context = context
        self.view_screenname = view_screenname
        self.view_title = view_title
        self.element_list = []

    def build(self):
        mimetype = self.context.getHeader('Content-Type')

        result = "unknown"
        if mimetype == "application/json":
            result = self.toJson()
        else:
            result = self.toHtml()
        return result


    def getAsDict(self):
        return {
                "screenname": self.view_screenname,
                "title": self.view_title,
                "layout":{
                    "elements":self.element_list
                    }
                }

    def addElement(self, element):
        self.element_list.append(element.getAsDict())


    def toJson(self):
        return json.dumps(self.getAsDict())

    def toHtml(self):
        data = self.toJson()
        return render_template("index.html", data = data, screentitle = self.view_title)
