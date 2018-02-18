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

class visdom_recorder:
    def __init__(self):
        self.viz = Visdom()
        assert self.viz.check_connection(), 'Visdom server not started, python -m visdom-server and default port = 8097'
        self.windows = {}


    def add_scalar(self, tag, val, niter):
        assert val.size == 1, 'Only scalar is accepted'
        if tag not in self.windows.keys():
            lineplot = self.viz.line(Y=val, X=niter, opts=dict(showlegend=True, title=tag))
            self.windows[tag] = lineplot
        else:
            win = self.windows[tag]
            self.viz.line(
                X=niter,
                Y=val,
                win=win,
                update='append'
            )

    def add_images_grid(self, tag, x, niter):
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
