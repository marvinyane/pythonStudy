#! /usr/bin/env python

import sys, logging
from wsgilog import WsgiLog
import config

class Log(WsgiLog):
    def __init__(self, application):
        WsgiLog.__init__(
                self,
                application,
                logformat = '%(message)s',
                tofile = True,
                file = config.log_file,
                interval = config.log_interval,
                backups = config.log_backups
                )

        sys.stdout = wsgilog.LogIO(self.logger, logging.INFO)
        sys.stderr = wsgilog.LogIO(self.logger, logging.ERROR)
