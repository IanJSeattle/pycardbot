# vi: set expandtab ai:

import os
import yaml

class Config(object):
    """ instantiating this class reads in all the config files """

    # the fields which are allowed in the config file
    _fields = ['carddir', 'default_channel', 'my_nick', 'server', 'port',
        'turns', 'min_players', 'max_players', 'text', 'language',
        'hand_size', 'logfile', 'max_points']

    def __init__(self):
        self.path = ['.', '..'] # the last config.yaml found will win
        self.data = {}
        self.read_files()

    def fake_get(self, name):
        if name == 'default_channel':
            return '#test'
        if name == 'carddir':
            return 'cards'

    def read_files(self):
        for path in self.path:
            filename = '{}/config.yaml'.format(path)
            if os.path.isfile(filename):
                with open(filename, 'r') as fp:
                    data = yaml.load(fp.read())
                    self.data = data
                    self.check_config()

    def check_config(self):
        for name in self.data:
            if name not in self._fields:
                raise ValueError('{} is not a known config field'.format(name))

    def reload(self):
        self.read_files()
