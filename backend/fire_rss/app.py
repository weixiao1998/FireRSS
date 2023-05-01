import importlib

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from . import views
from .base.db import init_peewee
from .base.restful import init_error_handler

app = Flask(__name__)
api_app = Flask("api")
init_peewee(api_app)
init_error_handler(api_app)

for view in views.api_views:
    bpt = importlib.import_module(f"{views.__package__}.{view}").BPT
    if bpt.url_prefix is None:
        bpt.url_prefix = "/" + bpt.name.lstrip("/")
    api_app.register_blueprint(bpt)

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {"/api": api_app},
)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
