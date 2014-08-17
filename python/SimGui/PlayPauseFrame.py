#!/usr/bin/python
'''
\brief GUI frame which allows the user to pause the simulation.

\author Thomas Watteyne <watteyne@eecs.berkeley.edu>
\author Xavier Vilajosana <xvilajosana@eecs.berkeley.edu>
\author Kazushi Muraoka <k-muraoka@eecs.berkeley.edu>
\author Nicola Accettura <nicola.accettura@eecs.berkeley.edu>
'''

#============================ logging =========================================

import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
log = logging.getLogger('PlayPauseFrame')
log.setLevel(logging.ERROR)
log.addHandler(NullHandler())

#============================ imports =========================================

import Tkinter
import threading

from SimEngine import SimEngine, \
                      SimSettings

#============================ defines =========================================

#============================ body ============================================

class PlayPauseFrame(Tkinter.Frame):
    
    def __init__(self,guiParent):
        
        # store params
        self.guiParent  = guiParent
        
        # initialize the parent class
        Tkinter.Frame.__init__(
            self,
            self.guiParent,
            relief      = Tkinter.RIDGE,
            borderwidth = 1,
        )
        
        # GUI layout
        self.nextCycleButton = Tkinter.Button(self, text="nextCycle",command=self._nextCycle_clicked)
        self.nextCycleButton.grid(row=0,column=0)
        self.nextRunButton   = Tkinter.Button(self, text="nextRun",  command=self._nextRun_clicked)
        self.nextRunButton.grid(row=1,column=0)
        self.goButton        = Tkinter.Button(self, text="go",       command=self._go_clicked)
        self.goButton.grid(row=2,column=0)
    
    #======================== public ==========================================
    
    def close(self):
        pass
    
    #======================== attributes ======================================
    
    @property
    def engine(self):
        return SimEngine.SimEngine(failIfNotInit=True)
    
    @property
    def settings(self):
        return SimSettings.SimSettings(failIfNotInit=True)
    
    #======================== private =========================================
    
    def _nextCycle_clicked(self):
        print 'nextCycle clicked'
        try:
            nowAsn           = self.engine.getAsn()
            endCycleAsn      = nowAsn+self.settings.slotframeLength-(nowAsn%self.settings.slotframeLength)
            
            self.engine.pauseAtAsn(
                asn          = endCycleAsn,
            )
        except EnvironmentError:
            # this happens when we try to update between runs
            pass
    
    def _nextRun_clicked(self):
        print "TODO _nextRun_clicked"
    
    def _go_clicked(self):
        print 'go clicked'
        try:
            self.engine.go()
        except EnvironmentError:
            # this happens when we try to update between runs
            pass
    