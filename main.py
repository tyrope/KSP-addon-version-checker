#!/usr/bin/env python2.7
#coding: utf8

"""
KSP Add-on Version Checker.
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

import config
import os, sys
import versionComparator as verComp

def main():
    # Find config folder.
    cfg_dir = os.path.join(os.path.expanduser('~'), '.KSP-AVC')
    # Create it if needed.
    if not os.path.exists(cfg_dir):
        os.makedirs(cfg_dir)

    # Create config object.
    cfg = config.Config(os.path.join(cfg_dir, 'default.cfg'))

    for mod in findMods(cfg):
        remote = verComp.getRemote(mod)
        print "Found version file %s reporting remote %s" % (mod, remote)
        # comp = verComp.versionComparator(mod, remote)

    #Shutdown procedure
    cfg.save()
    sys.exit(0)

def findMods(cfg):
    mods = set()
    # Walk through the directories
    for path, folders, files in os.walk(cfg.get('gamedata_dir')):
        # Walk through the files.
        for f in files:
            # Found a version file.
            if f.lower().endswith(".version"):
                mods.add(os.path.join(path, f))
    return mods

# Startup sequence
if __name__ == '__main__':
    main()

