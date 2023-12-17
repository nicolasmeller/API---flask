# response_handler.py
from json import dumps
from flask import jsonify

class Response:
    def __init__(self, response):
        self.response = response
        
    def json(self):
        return jsonify(self.response)
    
    def text(self):
         return str(self.response)