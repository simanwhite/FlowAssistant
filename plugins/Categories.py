import os
from yapsy.IPlugin import IPlugin


class BasicPlugin(IPlugin):
    name = 'Basic Plugin'

    def __init__(self):
        super(BasicPlugin, self).__init__()
        print 'do nothing here'


class TabularPlugin(IPlugin):
    name = 'Tabular Plugin'
    _this_directory = os.path.dirname(__file__)
    icon = '%s/default_res/alarm.gif' % _this_directory

    def __init__(self):
        super(TabularPlugin, self).__init__()
        print 'init of tabular plugin'
