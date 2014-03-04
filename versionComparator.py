#coding: utf8
"""
The versionComparator class uses 2
provided *.version files and
allows comparing of the contents.
"""
# Copyright 2014 Dimitri "Tyrope" Molenaars

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json, os
from urllib2 import urlopen

class versionComparator(object):
    """ Initialize the comparator. """
    def __init__(self, l, r):
        with open(l, 'r') as f:
            self.local = json.load(f)
        f = urlopen(r)
        self.remote = json.load(f)
        f.close()

    """ Are the major versions equal? """
    def compareMajor(self):
        return self.local['VERSION']['MAJOR'] == self.remote['VERSION']['MAJOR']

    """ Are the minor versions equal? """
    def compareMinor(self):
        return self.local['VERSION']['MINOR'] == self.remote['VERSION']['MINOR']

    def getVersion(self, side):
        if side in ('l','local'):
            v = self.local
        elif side in ('r', 'remote'):
            v = self.remote
        else:
            return '0.0'
        return '%s.%s' % (v['VERSION']['MAJOR'], v['VERSION']['MINOR'])

    """ Ensures the remote file is from the proper source.
    If this returns false, the remote file failed loading
    or something went terribly wrong. """
    def compareSource(self):
        return self.local['URL'] == self.remote['URL']

    """ Ensures the remote file is for the same mod.
    if this returns false, we're probably
    downloading the wrong file. """
    def compareName(self):
        return self.local['NAME'] == self.remote['NAME']

""" Gets the URL for the remote file as stated in the local file. """
def getRemote(fle):
    if not os.path.exists(fle):
        raise OSError("File not found.")

    with open(fle,'r') as f:
        json_dec = json.load(f)
    return json_dec['URL']

if __name__ == '__main__':
    print __doc__

