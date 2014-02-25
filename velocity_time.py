import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

plt.rcParams["legend.fontsize"] = "small"
plt.rcParams['figure.figsize'] = 6, 3
#plt.rcParams['figure.dpi'] = 300

data = sio.loadmat('velocity_value.mat')
velocity = data['velocity']
velofit = data['velofit']
t = data['t']


plt.plot(t,velocity,'r.--',label="Estimated velocity",linewidth=1.5)
plt.plot(t,velofit,'b-',label="Fitted velocity",linewidth=1.5)
plt.ylabel('velocity (rpm)')
plt.xlabel('time (s)')
plt.xlim (0,1.2)
plt.ylim (0,18)
plt.legend(loc=0, ncol=2, shadow=False)
plt.tight_layout()

plt.savefig("velocity_time.eps",bbox_inches='tight',dpi=600)
plt.savefig("velocity_time.pdf",bbox_inches='tight',dpi=600)
plt.savefig("velocity_time.tif",bbox_inches='tight',dpi=600)

plt.show()