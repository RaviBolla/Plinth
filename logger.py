import cherrypy
import inspect
import cfg


def init():
    """Initialize logging"""
    cherrypy.log.error_file = cfg.status_log_file
    cherrypy.log.access_file = cfg.access_log_file
    if not cfg.no_daemon:
        cherrypy.log.screen = False


class Logger(object):
    """By convention, log levels are DEBUG, INFO, WARNING, ERROR and CRITICAL."""
    def log(self, msg, level="DEBUG"):
        cherrypy.log.error("%s %s" % (level, msg), inspect.stack()[2][3], 20)
    def __call__(self, *args):
        self.log(*args)

    def debug(self, msg):
        self.log(msg)

    def info(self, msg):
        self.log(msg, "INFO")

    def warn(self, msg):
        self.log(msg, "WARNING")

    def warning(self, msg):
        self.log(msg, "WARNING")

    def error(self, msg):
        self.log(msg, "ERROR")

    def err(self, msg):
        self.error(msg)

    def critical(self, msg):
        self.log(msg, "CRITICAL")
