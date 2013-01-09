import simplejson

from django.http import HttpResponse

def json_response(data):
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def json_error(message):
    return json_response({'result': 'error', 'message': message})