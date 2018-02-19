from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from visdom import Visdom
import numpy as np
import math
import os.path
import getpass
from sys import platform as _platform
from six.moves import urllib
import time

class visdom_recorder:
    def __init__(self):
        self.viz = Visdom()
        time.sleep(1) #this is only necessary if your network is somehow slow like mine
        assert self.viz.check_connection(), 'Visdom server connection failed, start server with python -m visdom.server and default port = 8097'
        self.windows = {}


    def add_scalar(self, tag, val, niter):
        val, niter = map(lambda x : np.ones([1])*x, [val, niter]) #create array from scalar to make visdom happy
        if tag not in self.windows.keys():
            lineplot = self.viz.line(Y=val,X=niter, opts=dict(title=tag))
            self.windows[tag] = lineplot
        else:
            win = self.windows[tag]
            self.viz.line(
                Y=val,
                X=niter,
                win=win,
                update='append',
            )

    def add_image_grid(self, tag, x, niter):
        if tag not in self.windows.keys():
            grid = self.viz.images(
                x,
                opts=dict(title=tag, caption='At Iter {}'.format(niter))
            )
            self.windows[tag] = grid
        else:
            win = self.windows[tag]
            self.viz.images(
                x,
                win=win
            )
