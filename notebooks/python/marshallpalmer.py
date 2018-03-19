
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Marshall-Palmer" data-toc-modified-id="Marshall-Palmer-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Marshall Palmer</a></span></li><li><span><a href="#Rain-rate" data-toc-modified-id="Rain-rate-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Rain rate</a></span></li></ul></div>

# In[ ]:


### Rewrite the MP distribtuion as a function


# In[5]:


import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

def marshallpalmer(R):
    """
    marshall palmer size distribution
    given rainrate R in mm/hr, return
    n(D), the number concentration of drops with
    diameter D

    Parameters
    ----------
    R: float
        rainrate (mm/hr)

    Returns
    -------

    d: vector (float)
      drop diameters (cm)

    n: vector (float)
     the number distribution n(d) #m^{-3} mm^{-1}

    """
    D=np.arange(0,8,0.01)
    Dmm=D
    Dcm=D*0.1
    N0=0.08*1.e6*1.e-1 #m**{-3} mm^{-1}
    theLambda=41*R**(-0.21)
    n=N0*np.exp(-theLambda*Dcm)
    return Dcm,n

curve_dict={}
Rvals = [1,5,25]
for R in Rvals:
    diam,ndist = marshallpalmer(R)
    curve_dict[R] = ndist
fig, ax = plt.subplots(1,1,figsize=(10,8))
for R in Rvals:
    ax.semilogy(diam,curve_dict[R],label='{} mm/hr'.format(R))
ax.set_xlabel('Drop diameter (mm)')
ax.set_ylabel('$n(D) m^{-3} mm^{-1}$')
ax.set_title('Marshall Palmer distribution for three rain rates')
out=ax.legend(loc='best')


# ##  Marshall Palmer
# 
# - Confirm that the mean diameter of the Marshall Palmer distribution is $1/\Lambda$

# ## Rain rate
# 
# 
# - Calculate the precipitation flux (mm/hr) using  the Marshall Palmer size distribution and
# the fall speed of  `Villermaux and Bossa (2009)`_: `w = - \sqrt{\rho_l/\rho_{air} * g *D}` where
# D is the drop diameter and `\rho_l,\rho_{air}` are the liquid and air densities.  Show
# that you get about R=15 mm/hour back if you put in R=15 mm/hour into
# the size distribution.   
