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
from urllib2 import urlopen, HTTPError

class versionComparator(object):
    """ Initialize the comparator. """
    def __init__(self, l, r):
        with open(l, 'r') as f:
            try:
                self.local = json.load(f)
            except ValueError as e:
                print "Version file has an invalid format."
                self.valid = False
                return
        try:
            f = urlopen(r)
        except HTTPError as e:
            print "Failed to open remote for mod %s. Error: %s" % (self.local['NAME'], e)
            self.valid = False
            return
        try:
            self.remote = json.load(f)
        except ValueError as e:
            print "Failed to load remote for mod %s. Error: %s" % (self.local['NAME'], e)
            print r.split('/')[-1] #DEBUG
            self.valid = False
            return
        f.close()
        self.valid = True

    """ Are the add-on's major versions equal? """
    def compareMajor(self):
        return self.local['VERSION']['MAJOR'] == self.remote['VERSION']['MAJOR']

    """ Are the add-on's minor versions equal? """
    def compareMinor(self):
        return self.local['VERSION']['MINOR'] == self.remote['VERSION']['MINOR']

    """ Are the add-on's patches equal? """
    def comparePatch(self):
        return self.local['VERSION']['PATCH'] == self.remote['VERSION']['PATCH']

    """ Print a human readable version string. """
    def getVersion(self, side):
        if side in ('l','local'):
            v = self.local
        elif side in ('r', 'remote'):
            v = self.remote
        else:
            return '0.0'
        try:
            #KSP-AVC 0.3 lay-out
            return '%s.%s.%s' % (v['VERSION']['MAJOR'], v['VERSION']['MINOR'], v['VERSION']['PATCH'])
        except KeyError as e:
            #KSP-AVC 0.4 lay-out.
            return v['VERSION']

    """ shorthand for compareMajor and compareMinor and comparePatch """
    def compareVersion(self):
        try:
            #KSP-AVC 3.0 lay-out
            return self.compareMajor and self.compareMinor and self.comparePatch
        except KeyError as e:
            #KSP-AVC 0.4 lay-out.
            return self.local['VERSION'] == self.remote['VERSION']

    """ Compare the supported version of Kerbal Space Program for this add-on """
    def compareKSP(self):
        try:
            if not self.local['KSP_VERSION']['MAJOR'] == self.remote['KSP_VERSION']['MAJOR'] \
            or not self.local['KSP_VERSION']['MINOR'] == self.remote['KSP_VERSION']['MINOR'] \
            or not self.local['KSP_VERSION']['PATCH'] == self.remote['KSP_VERSION']['PATCH']:
                return False
            return True
        except KeyError as e:
            # The KSP_VERSION key or any of it's children is not found.
            # Let's be nice and assume it'll work.
            return True

    """ Ensures the remote file is from the proper source.
    If this returns false, the remote file failed loading
    or something went terribly wrong. """
    def compareURL(self):
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

