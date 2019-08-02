# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers as h


route_patterns = [
    url(r'^/promo/(?P<id>[^/]+)/?$', h.PromoCodeHandler, name='promo_code'),
    url(r'^/promo/?$', h.PromoCodeHandler, name='promo_code_create'),
    url(r'^/promo-list/?$', h.PromoCodeListHandler, name='promo_codes'),
    url(r'^/use-promo/(?P<id>[^/]+)/?$', h.UsePromoCode, name='use_promo_code'),
]
