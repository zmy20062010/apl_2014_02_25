import numpy as np
import scipy.io as sio

data = np.linspace(1,100,100);

sio.savemat('matlabfile',{'data':data});