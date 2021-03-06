import os

import falcon

from falcon_jinja2 import FalconTemplate

path = os.path.join(os.path.dirname(__file__), 'test_templates')
falcon_template = FalconTemplate(path=path)


class FirstResource:
    @falcon_template.render('index.html')
    def on_get(self, req, resp):
        resp.context = {'quote': 'Hello from Falcon!'}


class SecondResource:
    @falcon_template.render('second.html')
    def on_get(self, req, resp):
        resp.context = {'frameworks': ['Falcon', 'Flask', 'Django']}


app = falcon.API()
app.add_route('/first', FirstResource())
app.add_route('/second', SecondResource())
