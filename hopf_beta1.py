from pylab import figure, show, rand
from matplotlib.patches import Ellipse
import matplotlib as mpl
import numpy as np

num = 18
ang = 360/num-1
colorlist = mpl.cm.spectral(np.arange(num*20))
ells = [Ellipse(xy = ([5,5]), width = 3, height = 1, angle = i*ang) for i in range(num)]

fig = figure()
ax = fig.add_subplot(111, aspect = 'equal')
for i in range(num) :
    e = ells[i]
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(0.2)
    e.set_facecolor(colorlist[i*20])

ax.set_xlim(0,10)
ax.set_ylim(0,10)
