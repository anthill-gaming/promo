# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers


route_patterns = [
    url(r'^/promo/(?P<id>[^/]+)/?$', handlers.PromoCodeHandler, name='promo_code'),
    url(r'^/promo/?$', handlers.PromoCodeHandler, name='promo_code_create'),
    url(r'^/promo-list/?$', handlers.PromoCodeListHandler, name='promo_codes'),
    url(r'^/use-promo/(?P<id>[^/]+)/?$', handlers.UsePromoCode, name='use_promo_code'),
]
