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
plt.rcParams['figure.figsize'] = 5, 5
#plt.rcParams['figure.dpi'] = 300

data = sio.loadmat('velocity_polar.mat')
position = data['position']
velocity = data['velocity']


plt.polar(position,velocity,'r.--',label="Estimated velocity",linewidth=1.5)
plt.rgrids(velocity,'velocity (rpm)')
plt.thetagrids(position,'position (rad)')
plt.xlim (0,1.2)
plt.ylim (0,20)
plt.legend()
plt.tight_layout()

plt.savefig("velocity_posture.eps",bbox_inches='tight',dpi=600)
plt.savefig("velocity_posture.pdf",bbox_inches='tight',dpi=600)
plt.savefig("velocity_posture.tif",bbox_inches='tight',dpi=600)

plt.show()