import logging
import logging.config
import os

log_level = os.getenv('LOG_LEVEL', 'INFO')

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': log_level,
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': log_level,
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': 'app.log'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': log_level,
            'propagate': True
        },
    }
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
