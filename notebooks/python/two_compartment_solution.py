
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#First-find-the-total-mass-and-energy-before" data-toc-modified-id="First-find-the-total-mass-and-energy-before-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>First find the total mass and energy before</a></span></li><li><span><a href="#Use-the-specific-internal-energy-u-=-cv*T--to-find-T-after" data-toc-modified-id="Use-the-specific-internal-energy-u-=-cv*T--to-find-T-after-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Use the specific internal energy u = cv*T  to find T after</a></span></li><li><span><a href="#Use-the-equation-of-state-to-find-pressure-after" data-toc-modified-id="Use-the-equation-of-state-to-find-pressure-after-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Use the equation of state to find pressure after</a></span></li></ul></div>

# * Consider two compartments, each with a volume of 1 $m^3$, separated by a rigid, perfectly insulating membrane.
#  
# * Initially $T_A$ = 300 K and $p_A$ = $10^5$ Pa, and $T_B$ = 100 K and $p_B$ = $10^3$ Pa.  Suppose the membrane breaks.  Find the final temperature and pressure in the 2 $m^3$ compartment.   Does the total entropy change?  By how much?
# 
# 

# In[ ]:


from a405.thermo.thermlib import find_theta
import numpy as np
Ta=300  #K
pa=1.e5 #Pa
Tb =100 #K
pb =1.e3  #Pa
Rd = 287 #J/kg/K
cv = 717 #J/kg/K
cpd = 1004.  #J/kg/K
dens_fun = lambda temp,press: press/(Rd*temp)
theta_fun = lambda temp, press: temp*(1.e5/press)**(Rd/cpd)


# # First find the total mass and energy before

# In[ ]:


dens_a = dens_fun(Ta,pa)
dens_b = dens_fun(Tb,pb)
theta_a = find_theta(Ta,pa)
theta_b = find_theta(Ta,pb)
#
# total mass = sum of mass of two 1 m^3 compartments
#
Mtot = dens_a*1 + dens_b*1
Ua = dens_a*cv*Ta  #internal energy in Joules
Ub = dens_b*cv*Tb
Utot = Ua + Ub


# # Use the specific internal energy u = cv*T  to find T after

# In[ ]:


u_tot = Utot/Mtot  #specific internal energy in J/kg
temp_after = u_tot/cv


# # Use the equation of state to find pressure after

# In[20]:


dens_after = Mtot/2.  #total volume is 2 m**3.
press_after = Rd*dens_after*temp_after
theta_after = find_theta(temp_after,press_after)
entropy_before= dens_a*cpd*np.log(theta_a) + dens_b*cpd*np.log(theta_b)
entropy_after = Mtot*cpd*np.log(theta_after)


# In[21]:


entropy_after,entropy_before

