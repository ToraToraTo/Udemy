import logging
# loggingのフォーマッターについて
formatter = '%(levelname)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)


logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')