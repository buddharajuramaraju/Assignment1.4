
# coding: utf-8

# ### Problem Statement
# 
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r^3

# In[6]:


from fractions import Fraction # to calculate fraction values
import math # to get math.pi value

sphere_diameter = 12 ## given value 12 cm

r = sphere_diameter/2 ## r = d/2



# In[9]:


sphere_volume = Fraction(4,3) * math.pi * (r**3) 


# In[11]:


print ("Given sphere volume is {Volume} cm^3".format(Volume=sphere_volume))

