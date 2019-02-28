#!/usr/bin/env python3

from rpyc_classic import *
from switch_device import *

class Baby_Monitor(SwitchDevice):
    def get_name(self):
        return 'Baby Monitor'

    def get_label(self):
        return 'Current State'

my_device = Baby_Monitor()
my_device.value = False

ClassicServer.host = '127.0.0.4'
ClassicServer.run()

