from .errors import DisabledDistAPIError, UndefinedExtStateError
from urllib import request
from urllib.error import URLError

import json

class WebInterface:

    def __init__(self, port):
        self._url = "http://localhost:{}/_/".format(port)
        self.ext_state = ExtendedState(self)
        
    def activate_reapy_server(self):
        try:
            script_id = self.ext_state["activate_reapy_server:id"]
            self.perform_action(script_id)
        except UndefinedExtStateError:
            raise DisabledDistAPIError
    
    def get_reapy_server_port(self):
        try:
            port = self.ext_state["server_port"]
        except URLError:
            raise DisabledDistAPIError
        except UndefinedExtStateError:
            self.activate_reapy_server()
            port = self.get_reapy_server_port()
        return port
        
    def perform_action(self, action_id):
        url = self._url + str(action_id)
        request.urlopen(url)
        
class ExtendedState:

    def __init__(self, web_interface):
        self._url = web_interface._url + "{method}/EXTSTATE/reapy/{key}"

    def __getitem__(self, key):
        url = self._url.format(method="GET", key=key)
        string = request.urlopen(url).read()
        value = string.split("\t")[-1][:-1]
        if not value:
            raise UndefinedExtStateError(key)
        value = json.loads(value)
        return value
        
    def __setitem__(self, key, value):
        value = json.dumps(value)
        url = self._url + "/{value}"
        url = url.format(method="SET", key=key, value=value)
        request.urlopen(url)