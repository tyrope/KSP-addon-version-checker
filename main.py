#!/usr/bin/env python2.7
#coding: utf8

"""
KSP Add-on Version Checker.
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

from config import Config
import os
import versionComparator

def main():
    cf = os.path.join(os.path.expanduser('~'), '.KSP-AVC','default.cfg')
    cfg = Config(cf)
    print cfg.get('install_dir')


    #Shutdown procedure
    if cfg.need_save():
        cfg.save()
    sys.exit(0)

if __name__ == '__main__':
    main()
