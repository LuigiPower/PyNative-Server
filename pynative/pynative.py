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

    def render(self, screen):
        mimetype = self.getHeader('Content-Type')

        result = "unknown"
        if mimetype == "application/json":
            result = screen.get_json()
        else:
            json = screen.get_json()
            result = render_template("index.html", data = json, pagetitle = screen.data['title'])
        return result

#class ElementBuilder():
#
#    json = {}
#
#    def __init__(self, jsoninit):
#        self.json = jsoninit
#
#    @classmethod
#    def createTextView(cls, el_id, text):
#        json = {
#                "type": "textview",
#                "id": el_id,
#                "text": text
#            }
#
#        return cls(json)
#
#    @classmethod
#    def createGotoButton(cls, el_id, text, toScreen):
#        json = {
#                "type": "button",
#                "id": el_id,
#                "text": text,
#                "action": {
#                    "type": "goto",
#                    "screen": toScreen
#                    }
#                }
#
#        return cls(json)
#
#    def getAsDict(self):
#        return self.json



#class ViewBuilder():
#
#    def __init__(self, context, screen):
#        self.context = context
#        self.screen = screen
#
#    def build(self):
#        mimetype = self.context.getHeader('Content-Type')
#
#        result = "unknown"
#        if mimetype == "application/json":
#            result = self.toJson()
#        else:
#            result = self.toHtml()
#        return result
#
#
#    def getAsDict(self):
#        return self.screen.data
#
#    def toHtml(self):
#        data = self.toJson()
#        return render_template("index.html", data = data, screentitle = self.view_title)
