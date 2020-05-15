import logging
import sys

from dogebuild.doge import _main


class DogeController:

    def __init__(self, args):
        self._config_logging()

    def run(self) -> int:
        _main()
        return 0

    @staticmethod
    def _config_logging():
        console_format = '{log_color}{name}: {message}{reset}'
        console_level = 'DEBUG'

        logging.config.dictConfig({
            'version': 1,
            'formatters': {
                'colored': {
                    '()': 'colorlog.ColoredFormatter',
                    'format': console_format,
                    'style': '{',
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'colored',
                    'level': console_level,
                    'stream': sys.stdout,
                },
            },
            'loggers': {
                '': {
                    'handlers': ['console'],
                    'level': console_level,
                },
            },
        })