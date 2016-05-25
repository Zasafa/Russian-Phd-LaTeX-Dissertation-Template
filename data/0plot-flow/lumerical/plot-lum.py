#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'font.size': 16})


def fieldplot(fig, ax, data, x, comment='', WL_units='nm',
              npts=301, outline_width=1, subplot_label=' '):
   
    try:
        from matplotlib import cm
        from matplotlib.colors import LogNorm
        Eabs_data = data
        label = r'$|E|/|E_0|$'
        
        # Rescale to better show the axes
        scale_x = np.linspace( -150, 150, npts)
        scale_z = np.linspace( -150, 150, npts)

        ax.locator_params(nbins=5)

        # # Define scale ticks
        # min_tick = np.amin(Eabs_data[~np.isnan(Eabs_data)])
        # max_tick = np.amax(Eabs_data[~np.isnan(Eabs_data)])
        min_tick = 0.1
        #max_tick = 8.58
        max_tick = 7.0
        scale_ticks = np.linspace(min_tick, max_tick, 5)
        #scale_ticks = np.power(10.0, np.linspace(np.log10(min_tick), np.log10(max_tick), 6))
        #scale_ticks = [0.1,0.3,1,3,10, max_tick]
        # Interpolation can be 'nearest', 'bilinear' or 'bicubic'
        # ax.set_title(label)
        # build a rectangle in axes coords
        ax.annotate(subplot_label, xy=(0.0, 1.1), xycoords='axes fraction',  # fontsize=10,
                    horizontalalignment='left', verticalalignment='top')
        ax.xaxis.set_tick_params(width=outline_width/2.0)
        ax.yaxis.set_tick_params(width=outline_width/2.0)
        # ax.text(right, top, subplot_label,
        #         horizontalalignment='right',
        #         verticalalignment='bottom',
        #         transform=ax.transAxes)
        cax = ax.imshow(Eabs_data, interpolation='nearest', cmap=cm.jet,
                        origin='lower', vmin=min_tick, vmax=max_tick, extent=(min(scale_x), max(scale_x), min(scale_z), max(scale_z))
                        # ,norm = LogNorm()
                        )
        ax.axis("image")

        # Add colorbar
        cbar = fig.colorbar(cax, ticks=[a for a in scale_ticks], ax=ax)
        # vertically oriented colorbar
        cbar.ax.set_yticklabels(['%3.2f' % (a) for a in scale_ticks])
        # pos = list(cbar.ax.get_position().bounds)
        #fig.text(pos[0] - 0.02, 0.925, '|E|/|E$_0$|', fontsize = 14)
        lp2 = -15.0
        lp1 = -1.0
        ax.set_xlabel('Z, ' + WL_units, labelpad=lp1)
        ax.set_ylabel('X, ' + WL_units, labelpad=lp2)
        # # This part draws the nanoshell
        from matplotlib import patches
        from matplotlib.path import Path
        # for xx in [x[0],x[-1]]:
        for xx in x:
            r = xx * WL / 2.0 / np.pi
            s1 = patches.Arc((0.5, 0.5), 2.0 * r+0.5, 2.0 * r+0.5,  angle=0.0, zorder=1.8,
                             theta1=0.0, theta2=360.0, linewidth=outline_width, color='black')
            ax.add_patch(s1)

    finally:
        print("Done")
    #

    
fname='SiAgSi-at-800.txt'
data = np.loadtxt(fname)
fig, axs = plt.subplots(1,1)#, sharey=True, sharex=True)
fig.tight_layout()
WL=800 #nm
core_width = 17.74 #nm Si
inner_width = 23.31 #nm Ag
outer_width = 22.95 #nm  Si

core_r = core_width
inner_r = core_r+inner_width
outer_r = inner_r+outer_width

# n1 = 1.53413
# n2 = 0.565838 + 7.23262j
nm = 1.0

x = np.ones((3), dtype = np.float64)
x[0] = 2.0*np.pi*core_r/WL
x[1] = 2.0*np.pi*inner_r/WL
x[2] = 2.0*np.pi*outer_r/WL

fieldplot(fig, axs, data.T,x)
fig.subplots_adjust(hspace=0.3, wspace=-0.1)

plt.savefig("lumerical"+"-R"+str(int(round(x[-1]*WL/2.0/np.pi)))+"-XZ-Eabs.pdf",pad_inches=0.02, bbox_inches='tight')

plt.draw()

#    plt.show()

plt.clf()
plt.close()
