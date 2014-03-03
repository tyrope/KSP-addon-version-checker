#coding: utf8
"""
Config Module for KSP Add-on Version Checker.
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

import ConfigParser
import os

class ConfigError(Exception):
    def __init__(self,v):
        self.value = v
    def __str__(self):
        return 'ConfigError: %s' % self.value

class Config(object):

    needs_save = False

    def __init__(self, fn):
        """Get a config object to play with.
        Arguments: fn = path to config file.
        """
        self.configFile = fn

        self.parser = ConfigParser.RawConfigParser()
        self.parser.read(self.configFile)

        #Create sections if not available.
        if not self.parser.has_section('KSP'):
            self.parser.add_section('KSP')

        # Create default values if needed.
        if not self.parser.has_option('KSP','install_dir'):
            v = raw_input(
            "Where did you install KSP?"+
            "[e.g. C:\Program Files\Kerbal Space Program]: ")
            if v.endswith('/') or v.endswith('\\'):
                #remove trailing slash
                v = v[:-1]
            if v.endswith("gamedata"):
                v = v[:-9]
            self.parser.set('KSP', 'install_dir', v)
            needs_save = True
        self.save()

    def get(self, key, cat="KSP"):
        """Get a value from the configuration file."""
        if not self.parser.has_section(cat):
            raise ConfigError('Section %s not found.' % cat)
            return None
        if not self.parser.has_option(cat, key):
            raise ConfigError('Value %s.%s not found.' % (cat, key))
            return None
        return self.parser.get(cat, key)

    def save(self):
        """ Save configs to file. """
        if(self.needs_save):
            with open(self.configFile, 'w') as f:
                self.parser.write(f)
                f.flush()
            self.needs_save = False

if __name__ == '__main__':
    print __doc__

