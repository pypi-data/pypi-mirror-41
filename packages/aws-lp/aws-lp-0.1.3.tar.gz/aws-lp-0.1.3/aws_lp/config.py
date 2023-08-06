"""Configuration handler class."""
from __future__ import unicode_literals

import os

from six.moves import configparser


class Config(object):
    """Configuration handler class."""

    def __init__(self, config_section='default'):
        self.config_name = 'aws_lp.conf'
        self.config_section = config_section

        if os.path.isdir(os.path.expanduser('~/.config')):
            self.config_file = os.path.expanduser(
                '~/.config/' + self.config_name)
        else:
            self.config_file = os.path.expanduser('~/.' + self.config_name)

        self.configparser = configparser.ConfigParser()

    def set_config(self, **kwargs):
        """Update config values."""
        if self.config_section not in self.configparser.sections():
            self.configparser.add_section(self.config_section)

        for (key, value) in kwargs.items():
            self.configparser.set(self.config_section, key, value)

        with open(self.config_file, 'w') as config_file:
            self.configparser.write(config_file)

    def get_config(self):
        """Return stored config."""
        if not os.path.isfile(self.config_file):
            return {}

        self.configparser.read(self.config_file)

        try:
            config = dict(self.configparser.items(self.config_section))
        except configparser.NoSectionError:
            return {}

        return config
