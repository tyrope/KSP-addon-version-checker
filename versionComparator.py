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

class versionComparator(object):
    """ Initialize the comparator. """
    def __init__(self, l, r):
        with open(l, 'r') as f:
            self.local = json.load(f)
        with open(r, 'r') as f:
            self.remote = json.load(f)

    """ Gets the version in a tuple from a decoded json file. """
    def getVersion(json):
        ver = json['VERSION']
        return (ver['MAJOR'], ver['MINOR'])

    """ Returns changes in major version.
    0 = no change
    1 = local file is outdated.
    -1 = Either of the files are invalid. """
    def compareMajor(self):
        v1 = getVersion(self.local)[0]
        v2 = getVersion(self.remote)[0]
        if v1 == v2:
            return 0
        if v1 < v2:
            return 1

    """ Returns changes in minor version.
    0 = no change
    1 = local file is outdated.
    -1 = Either of the files are invalid. """
    def compareMinor(self):
        v1 = getVersion(self.local)[1]
        v2 = getVersion(self.remote)[1]
        if v1 == v2:
            return 0
        if v1 < v2:
            return 1

    """ Ensures the remote file is from the proper source.
    If self returns false, the remote file failed loading
    or something went terribly wrong. """
    def compareSource(self):
        return self.localfile['URL'] == self.remote['URL']

""" Gets the URL for the remote file as stated in the local file. """
def getRemote(fle):
    if not os.path.exists(fle):
        raise OSError("File not found.")

    with open(fle,'r') as f:
        json_dec = json.load(f)
    return json_dec['URL']

if __name__ == '__main__':
    print __doc__

