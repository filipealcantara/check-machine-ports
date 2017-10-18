
"""Script to check the ports on a machine"""
### IMPORTS ###
import socket
import logging
from logging.handlers import SysLogHandler

### GLOBAL VARS ###
DNSS = [
    "domain.co"
]
PAPERTRAIL_PORT = 123456
PORT_TO_CHECK = 9200 # i.e elasticsearch

### CLASSES ###
class ContextFilter(logging.Filter):
    """Class to define the hostname variable"""
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True


### EXECUTION ###
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

F = ContextFilter()
LOGGER.addFilter(F)

SYSLOG = SysLogHandler(address=('logs3.papertrailapp.com', PAPERTRAIL_PORT))
FORMATTER = logging.Formatter(
    '%(asctime)s port-checker app.py: %(message)s',
    datefmt='%b %d %H:%M:%S'
)

SYSLOG.setFormatter(FORMATTER)
LOGGER.addHandler(SYSLOG)

for dns in DNSS:
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.settimeout(10.0)
    RESULT = SOCK.connect_ex((dns, PORT_TO_CHECK))
    if RESULT == 0:
        LOGGER.info("[WARN ] port OPEN on " + dns)
        SOCK.close()
    else:
        LOGGER.info("[INFO ] port CLOSED on " + dns)

### CLEAN EXIT ###
raise SystemExit(0)
