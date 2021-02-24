"""
:author: Alex Robinson <girotobial@gmail.com>
:copyright: Copyright (c) Alex Robinson, 2021-2021.
:license: MIT
"""

import re
from .enums import Unit
from .constant import METRIC_RE


class Tire:
    def __init__(self, size: str):
        self.size = size
        self.unit = Unit.METRIC if re.match(METRIC_RE, self.size) else Unit.IMPERIAL

