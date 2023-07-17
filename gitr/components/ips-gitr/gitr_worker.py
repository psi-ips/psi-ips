#! /usr/bin/env python

from ipsframework import Component
import gitr
import os

class gitr_worker(Component):
    def __init__(self, services, config):
        Component.__init__(self, services, config)
        print('Created %s' % (self.__class__))

    def init(self, timeStamp=0.0):
        #Set up input deck
        print(('input dir and cwd this now', self.GITR_INPUT_DIR, ' ', os.getcwd()))
        gitr.copy_folder(self.GITR_INPUT_DIR,os.getcwd())
        print('done copying, beginning modify inpyt')

        gitr.modifyInputParam(nT=int(self.NT),nP=int(self.NP))
        print('done modifying, returning to driver')
        return

    def step(self, timeStamp=0.0):
        print('Hello from gitr_worker')
        self.services.stage_state()
        print('done staging, return')
        os.environ['OMP_NUM_THREADS'] = self.THREADS_PER_TASK
        task_id = self.services.launch_task(self.NPROC,
                                            self.services.get_working_dir(),
                                            self.GITR_EXE,task_ppn=self.TASK_PPN,
                                            logfile='gitr.log') #,ppn=1)
        #monitor task until complete
        if (self.services.wait_task(task_id)):
            self.services.error('gitr_comp: step failed.')
        print('Finished worker step')
        return
    
    def finalize(self, timeStamp=0.0):
        return
    
