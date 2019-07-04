# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from anthill.framework.utils.urls import include
from .api.compat.rest import routes as rest_routes
from tornado.web import url
from . import handlers

# Create your routes here.
route_patterns = [
    url(r'^/', include(rest_routes.route_patterns, namespace='api')),  # for compatibility only
]
