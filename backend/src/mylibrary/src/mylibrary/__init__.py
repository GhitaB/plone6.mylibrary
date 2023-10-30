"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "mylibrary"

_ = MessageFactory("mylibrary")

logger = logging.getLogger("mylibrary")
