import json

#   Target JSON:
#   {
#       "screenname": name,
#       "title": title,
#       "layout": {
#           "views": [
#               <element1>,
#               <element2>,
#               . . .,
#               <elementN>
#           ]
#       }
#   }
#
#   <element> :
#
#   {
#       "type": type, //one of the classnames (ex.: view, textview...)
#       "id": id, //If not specified, __
#       "parameters": {
#           <type-specific parameters>
#       }
#   }
#
#

class Screen(object):
    def __init__(self, name = "MainScreen", title = "PyNative!"):
        self.data = {
                "screenname": name,
                "title": title,
                "parameters": {
                    "layout": {
                        "views": []
                        }
                    }
                }

        self.views = []

    def add_view(self, view):
        self.views.append(view)
        self.data['parameters']['layout']['views'].append(view.data)
        print "Data is %s" % json.dumps(self.data)

    def get_type(self):
        return self.__name__.lower()

    def get_data(self):
        return self.data

    def get_json(self):
        return json.dumps(self.data)

class View(object):

    def __init__(self, vid = "__", start_data = None):
        if start_data is None:
            start_data = {}
        start_data['id'] = vid
        start_data['type'] = self.get_type()
        start_data['parameters'] = {}
        start_data['parameters']['width'] = 'wrap_content'  #TODO implement
        start_data['parameters']['height'] = 'wrap_content' #TODO implement
        start_data['parameters']['events'] = {}

        self.data = start_data

    def get_type(self):
        return type(self).__name__.lower()

    def get_data(self):
        return self.data

    def get_json(self):
        return json.dumps(self.data)

class TextView(View):

    def __init__(self, text = "TextView", vid = "__", start_data = None):
        super(TextView, self).__init__(vid = vid, start_data = start_data)

        self.data['parameters']['text'] = text

    def set_text(self, text):
        self.data['parameters']['text'] = text

class Button(TextView):

    def __init__(self, text = "Button", vid = "__", start_data = None):
        super(Button, self).__init__(text = text, vid = vid, start_data = start_data)

    def add_event(self, event_type, event_action):   #TODO create a class Action for event_action?
        """ Adds an event to specified Button
        event_type is the type of the event (onclick, onlongclick...)
        event_action is what to do when pressed (goto, do...)
        """

        self.data['parameters']['events'].update({ event_type: event_action })

class ViewGroup(View):

    def __init__(self, vid = "__", start_data = None):
        super(ViewGroup, self).__init__(vid = vid, start_data = start_data)

        self.data['parameters']['layout'] = {}
        self.data['parameters']['layout']['views'] = []
        self.views = []

    def add_element(view):
        self.views.append(view)
        self.data['parameters']['layout']['views'].append(view.data)

