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
    #TODO Don't hardcode the file name.
    cfg = config.Config(os.path.join(cfg_dir, 'default.cfg'))
    print "Configuration file loaded."

    toUpdate = set()
    for mod in findMods(cfg):
        remote = verComp.getRemote(mod)
        comp = verComp.versionComparator(mod, remote)
        modname = comp.local['NAME']
        print "Checking %s" % modname
        if not comp.compareName():
            print "  [ERROR] Online version file is for different mod (%s)." % comp.remote['NAME']
            print "          This is very bad. Check this mod's version manually!"
            continue
        if not comp.compareSource():
            print "  [WARNING] Online version has the wrong URL. A new version"
            print "            might be available at a new download location."

        if not comp.compareMajor() or not comp.compareMinor():
            print "  [UPDATE] Latest version: %s, Installed version: %s" % (
                comp.getVersion('l'),
                comp.getVersion('r'))
            toUpdate.add(modname)
        elif not comp.compareBuild():
            print "  [UPDATE] A new build (%s) is available for version %s." % (
                comp.getBuild('r'), comp.getVersion('r'))
            print "           New builds don't usually change enough to warrant updating."
            print "           But it probably fixed a bug or 2. (You have build %s)" % comp.getBuild('l')
        print ""
    # End for
    print "You should update the following add-ons:"
    print "    "+', '.join(toUpdate)



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

