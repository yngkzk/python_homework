import logger

Logger = logger.Logger

log = Logger(Logger.DEBUG)
# log = Logger(Logger.DEBUG, file='myapp.log')

log.w('This is warning message', 1, 2, 3)
log.t('This is trace message', 4, 5, 6)
log.e('This is error message', 7, 8, 9)

log.set(log.TRACE)

log.t('This is trace message', 4, 5, 6)