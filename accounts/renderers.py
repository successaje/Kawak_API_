import pdb
import json

from email import charset
from encodings import utf_8
from urllib import response

from rest_framework import renderers

class UserRenderer(renderers.JSONRenderer):
    
    charset="utf_8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''

        #pdb.set_trace()

        if "ErrorDetail" in str(data):
            response = json.dumps({'errors':data})

        else:
            response = json.dumps({'data':data})

        return response