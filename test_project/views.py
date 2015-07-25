from pyramid.view import view_config
from pyramid.renderers import render_to_response
import json

@view_config(route_name='home')
def my_view(request):
    with open('selection.json') as json_file:
       senddata = json.load(json_file)
    for city in senddata:
        city['title'] = city['title'].replace('\n', '#');
    return render_to_response('templates/home.jinja2', {'senddata': senddata, 'size': len(senddata)}, request=request)
