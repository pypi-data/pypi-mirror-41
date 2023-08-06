"""
    Copyright (C) 2018 Team Kodi
    This file is part of Kodi - kodi.tv

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/README.md for more information.
"""

from .Addon import Addon

import gzip
import requests
import xml.etree.ElementTree as ET
from io import BytesIO


class Repository(object):
    def __init__(self, version, path):
        super(Repository, self).__init__()
        self.version = version
        self.path = path
        gz_file = requests.get(path, timeout=(10, 10)).content
        with gzip.open(BytesIO(gz_file), 'rb') as xml_file:
            content = xml_file.read()
        tree = ET.fromstring(content)
        self.addons = []
        for addon in tree.findall("addon"):
            self.addons.append(Addon(addon))

    def __contains__(self, addonId):
        for addon in self.addons:
            if addon.id == addonId:
                return True
        return False

    def find(self, addonId):
        for addon in self.addons:
            if addon.id == addonId:
                return addon
        return None

    def rdepends(self, addonId):
        rdepends = []
        for addon in self.addons:
            if addon.dependsOn(addonId):
                rdepends.append(addon)
        return rdepends
