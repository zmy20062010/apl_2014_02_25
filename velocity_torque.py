import numpy
import pylab as pl
import matplotlib.pyplot as plt
import math
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

plt.rcParams["legend.fontsize"] = "small"
plt.rcParams['figure.figsize'] = 4, 3
#plt.rcParams['figure.dpi'] = 300

t_max = 1.67
v_max = 84.95
t = numpy.linspace(0,1,21)
torque = t_max * t
velocity = v_max - v_max * t
#torque = numpy.multiply(numpy.array(0.0,0.01,1),t_max)
#velocity = numpy.subtract(v_max, numpy.multiply(v_max,numpy.array(0.0,0.01,1)))

plt.plot(torque,velocity,'ro-',linewidth=1.5)
plt.ylabel('velocity (rpm)')
plt.xlabel('torque (mNm)')
plt.xlim (0,1.8)
plt.ylim (0,90)
plt.legend(loc=0, ncol=3, shadow=False)
plt.tight_layout()

plt.savefig("velocity_torque.eps",bbox_inches='tight',dpi=600)
plt.savefig("velocity_torque.pdf",bbox_inches='tight',dpi=600)
plt.savefig("velocity_torque.tif",bbox_inches='tight',dpi=600)

plt.show()