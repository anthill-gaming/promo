from anthill.framework.utils.translation import translate_lazy as _
from anthill.platform.conf.settings import *
import os

# Build paths inside the application like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gfuj##umq24n7zaeejhig=72ytcp6s!n@wt1)rw&amp;*-c@ri20bo'

DEBUG = False

ADMINS = (
    ('Lysenko Vladimir', 'wofkin@gmail.com'),
)

SQLALCHEMY_DATABASE_URI = 'postgres://anthill_promo@/anthill_promo'

LOCATION = 'http://localhost:9612'
BROKER = 'amqp://guest:guest@localhost:5672'

# ROUTES_CONF = 'promo.routes'

# APPLICATION_CLASS = 'promo.apps.AnthillApplication'
APPLICATION_NAME = 'promo'
APPLICATION_VERBOSE_NAME = _('Promo')
APPLICATION_DESCRIPTION = _('Reward users with promo-codes')
APPLICATION_ICON_CLASS = 'icon-gift'
APPLICATION_COLOR = 'brown'

# SERVICE_CLASS = 'promo.services.Service'
TEMPLATE_PATH = os.path.join(BASE_DIR, 'ui', 'templates')
LOCALE_PATH = os.path.join(BASE_DIR, 'locale')

EMAIL_SUBJECT_PREFIX = '[Anthill: promo] '

CACHES["default"]["LOCATION"] = "redis://localhost:6379/22"
CACHES["default"]["KEY_PREFIX"] = "promo.anthill"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'anthill.framework.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'anthill.framework.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'anthill.server': {
            '()': 'anthill.framework.utils.log.ServerFormatter',
            'fmt': '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'color': False,
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'anthill.server',
        },
        'anthill.server': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT_DIR, 'promo.log'),
            'formatter': 'anthill.server',
            'maxBytes': 100 * 1024 * 1024,  # 100 MiB
            'backupCount': 10
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'anthill.framework.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'anthill': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'anthill.application': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'tornado.access': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'tornado.application': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'tornado.general': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'celery': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'celery.worker': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'celery.task': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'celery.redirected': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
        'asyncio': {
            'handlers': ['anthill.server'],
            'level': 'INFO',
            'propagate': False
        },
    }
}

#########
# GEOIP #
#########

GEOIP_PATH = os.path.join(BASE_DIR, '../')

#########
# HTTPS #
#########

# HTTPS = {
#     'key_file': os.path.join(BASE_DIR, '../server.key'),
#     'crt_file': os.path.join(BASE_DIR, '../server.crt'),
# }
HTTPS = None

############
# GRAPHENE #
############

GRAPHENE = {
    'SCHEMA': 'promo.api.v1.public.schema',
    'MIDDLEWARE': ()
}
