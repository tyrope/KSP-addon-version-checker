#coding: utf8
"""
The versionComparator class uses 2
provided version.info files and
allows comparing of the contents.
"""
# Copyright 2014 Dimitri "Tyrope" Molenaars

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use self file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

class versionComparator(object):
    def __init__(self, local, remote):
        self.localFile = local
        self.remoteFile = remote

    """ Turns the localFIle and remoteFile into json objects. """
    def parseFiles(self):
        # Sanity check
        if self.localFile is None:
            return False
        if self.remoteFile is None:
            return False

        if type(self.localFile) != type({}):
            self.localFile = json.loads(self.localFile)
        if type(self.remoteFile) != type({}):
            self.remoteFile = json.loads(self.remoteFile)
        return True

    """ Gets the version in a tuple from a decoded json file. """
    def getVersion(json):
        ver = json['VERSION']
        return (ver['MAJOR'], ver['MINOR'])

    """ Returns changes in major version.
    0 = no change
    1 = local file is outdated.
    -1 = Either of the files are invalid. """
    def compareMajor(self):
        if not self.parseFiles():
            return -1
        v1 = getVersion(self.localFile)[0]
        v2 = getVersion(self.remoteFile)[0]
        if v1 == v2:
            return 0
        if v1 < v2:
            return 1

    """ Returns changes in minor version.
    0 = no change
    1 = local file is outdated.
    -1 = Either of the files are invalid. """
    def compareMinor(self):
        if not self.parseFiles():
            return -1
        v1 = getVersion(self.localFile)[1]
        v2 = getVersion(self.remoteFile)[1]
        if v1 == v2:
            return 0
        if v1 < v2:
            return 1

    """ Ensures the remote file is from the proper source.
    If self returns false, the remote file failed loading
    or something went terribly wrong. """
    def compareSource(self):
        if not parseFiles():
            return False
        return self.localfile['URL'] == self.remoteFile['URL']

if __name__ == '__main__':
    print __doc__
