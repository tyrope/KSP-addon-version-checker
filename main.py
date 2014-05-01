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

    print "+----------------------------------------------+"
    print "| Kerbal Space Program Add-on Version Checker  |"
    print "| This program is not made by Squad, nor is it |"
    print "|        Officially recognized by them.        |"
    print "+----------------------------------------------+"

    try:
        selfVersionLocal = os.path.join(os.path.expanduser('.'), 'KSP-AVC.version')
        selfVersionRemote = verComp.getRemote(selfVersionLocal)
        comp = verComp.versionComparator(selfVersionLocal, selfVersionRemote)
        if not comp.compareName():
            raise Exception("Remote version file is for %s" % comp.remote['NAME'])
        if not comp.compareURL():
            raise Exception("Remote version file reports different URL.")
        if not comp.compareVersion():
            print "  [UPDATE] A new version(%s) of KSP-AVC is available. (You have %s)" % \
            (comp.getVersion('r'), comp.getVersion('l'))
    except Exception as e:
        print "[ERROR] Couldn't update KSP-AVC. %s" % e
        cfg.save()
        sys.exit(1)

    toUpdate = set()
    print "Starting add-on checks."
    for mod in findMods(cfg):
        remote = verComp.getRemote(mod)
        comp = verComp.versionComparator(mod, remote)
        if comp == False:
            continue
        modname = comp.local['NAME']
        print "[ADD-ON] %s" % modname
        if not comp.compareName():
            print "  [ERROR] Online version file is for different mod (%s)." % comp.remote['NAME']
            print "          This is very bad. Check this mod's version manually!"
            continue
        if not comp.compareURL():
            print "  [WARNING] Online version has the wrong URL. A new version"
            print "            might be available at a new download location."

        if not comp.compareVersion():
            print "  [UPDATE] Latest version: %s, Installed version: %s" % \
                (comp.getVersion('r'), comp.getVersion('l'))
            toUpdate.add(modname)
    # End for
    if len(toUpdate):
        print "%s add-ons found." % len(mods)
        print "You should update the following add-ons: "
        for mod in toUpdate:
            print "    %s." % (mod,)
    else:
        print "%s add-ons found, and none require an update!" % len(mods)

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

