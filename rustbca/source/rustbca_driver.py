#! /usr/bin/env python

import numpy as np
from ipsframework import Component

class rustbca_driver(Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)
        print('Created %s' % (self.__class__))

    def init(self, timeStamp=0.0):
        self.services.stage_input_files(self.INPUT_FILES)
        self.services.update_state()
        return

    def step(self, timeStamp=0.0):
        print('rustbca_driver: beginning step call') 
        try:
            worker_comp = self.services.get_port('WORKER')
        except Exception:
            self.services.exception('Error accessing worker component')
            raise
        # Loop over time
        TimeArray = np.array([0.0, 0.1, 0.2], dtype=float)
        for i in TimeArray:
            self.services.call(worker_comp, 'step', i)
        print('RustBCA Driver: finished worker call') 
        return

    def finalize(self, timeStamp=0.0):
        return

