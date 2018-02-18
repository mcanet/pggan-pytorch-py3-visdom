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


viz = Visdom()
time.sleep(1)
assert viz.check_connection(), 'Visdom server connection failed, start server with python -m visdom.server and default port = 8097'



Y = np.linspace(0, 4, 200)
Y = np.ones(1)
win = viz.line(
    Y=np.sqrt(Y) + 2,
    X=Y,
    env='banana',
    opts=dict(
        fillarea=True,
        showlegend=False,
        width=800,
        height=800,
        xlabel='Time',
        ylabel='Volume',
        ytype='log',
        title='Stacked area plot',
        marginleft=30,
        marginright=30,
        marginbottom=80,
        margintop=30,
    ),
)
# for i in range(100):
#     time.sleep(0.1)
#     print('awaken')
#     Y = Y + 1
#     viz.line(
#         Y = np.sqrt(Y) + 2,
#         X = Y,
#         win=win,
#         update='append'
#     )


win = viz.line(
    X=np.zeros(1),
    Y=np.ones(1)*10,
    opts=dict(title='banana')
)

for i in range(100000):
    viz.line(
        X=np.ones(1)*i,
        Y=np.ones(1)*i**2,
        win=win,
        update='append'
    )
    time.sleep(0.1)

