
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#plot-a-sounding" data-toc-modified-id="plot-a-sounding-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>plot a sounding</a></span></li></ul></div>

# In[7]:


def tryme(a,b,c,d):
    print(f'tryme got values {a}, {b}, {c}, {d}')
    
def tryme2(a=1,b=2):
    print(f'tryme2 got values {a}, {b}')
    
tryme(1,2,3,4)    
onestep=[1,2,3,4]
tryme(*onestep)

onedict=dict(a=5,b=6)
tryme2()
tryme2(b=7)
tryme2(**onedict)

begin, *middle, end = (0, 1, 2, 3, 4, 5)
print(f'begin={begin}, middle={middle}, end={end}')


# In[1]:


import numpy as np
from matplotlib import pyplot as plt
#!conda install -y pytz


# # plot a sounding

# In[2]:


from a405.soundings.wyominglib import read_soundings
from a405.skewT.skewlib import makeSkewDry
from a405.thermo.thermlib import convertTempToSkew
import datetime
import pytz

soundings= read_soundings('soundingdir')
print(soundings.keys())
print(soundings['sounding_dict'].keys())


# In[3]:


the_date=(2017,7,1,0)
the_sounding=soundings['sounding_dict'][the_date]
attributes=soundings['attributes']
#print(attributes)
fig,ax =plt.subplots(1,1,figsize=(8,8))
ax,skew = makeSkewDry(ax)
temp=the_sounding['temp']
press = the_sounding['pres']
tdew = the_sounding['dwpt']
temp_skew = convertTempToSkew(temp,press,skew)
tdew_skew = convertTempToSkew(tdew,press,skew)
ax.plot(temp_skew,press)
ax.plot(tdew_skew,press)
the_date=datetime.datetime(*the_date,tzinfo=pytz.utc)
central=pytz.timezone('US/Central')
the_date_central=the_date.astimezone(central)
title=f'Dodge City KS sounding: {str(the_date_central)}'
ax.set_title(title);
#help(convertTempToSkew)


# In[4]:


import time
print(dir(time))

