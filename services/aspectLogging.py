import logging

class LogAspect:
    _logger: logging.Logger
    _loggerInstances: dict[str, logging.Logger] = {}

    def __init__(self, aspect: str, logFormat: str = '%(asctime)s %(name)s :: %(levelname)-8s :: %(message)s',
                 logLevel: int = logging.INFO):
        if aspect in LogAspect._loggerInstances:
            self._logger = LogAspect._loggerInstances[aspect]
        else:
            self._logger = logging.getLogger(aspect)
            LogAspect._loggerInstances[aspect] = self._logger
            self._logger.setLevel(logLevel)
            logFileHandler = logging.FileHandler(aspect + '.log')
            logFileHandler.setLevel(logLevel)
            logFileHandler.setFormatter(logging.Formatter(fmt=logFormat, datefmt='%a %d %b %Y %H:%M:%S'))
            self._logger.addHandler(logFileHandler)

    def logger(self):
        return self._logger