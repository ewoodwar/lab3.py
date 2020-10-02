#!/usr/bin/env python
# coding: utf-8

# In[148]:


import matplotlib 
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from collections import OrderedDict
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

#Creating a df to work more easily with my data
df = np.loadtxt('PeakSepDataSet.txt', skiprows=1)

df


# In[72]:


#Split the data into seperate arrays so that we can access the arrays (columns) individually


# In[200]:


#making columns
Peak=df[:,1]
Shell=df[:,2]
Inc=df[:,3]


# # Part 1 (Data visualization- Global Overview)

# The visualization that we wish to explore is the relation between peak separation (Δj), shell parameter (Sj), and viewing inclination (Ij)
# 

# In[119]:


#Creating the first plot

fig1 = plt.figure()
ax1 = Axes3D(fig1)

ax1.scatter(Peak, Shell, Inc)
ax1.set_xlabel('Peak Seperation (km/s)')
ax1.set_ylabel('Shell parameter (unitless)')
ax1.set_zlabel('Viewing inclination (degrees)')
ax1.set_title('Global overview')
ax1.set_xlim3d(0, 500)
ax1.set_ylim3d(0.9,2)
ax1.set_zlim3d(0,90)

ax1.view_init(azim=0,elev=45)

plt.show()


# Above, some trends I notice are as follows: As there is an increase in Shell Parameter, there is also an increase in viewing inclination. Similarily, as there is an increase in Peak seperation, there is an increase in viewing inclination. 

# # Part 2

# Change the darkness of the plotted symbol according to the third variable, in matplotlib with the c and cmap arguments to the scatter function. 
# 
# Make this plot where white corresponds to a value of 0 and black to a value of 90 degrees, with a colourbar (the colorbar function) to indicate what the symbol colours mean. 

# In[153]:


viridis = cm.get_cmap('viridis', 90)
print(viridis)

print(viridis(0.56))


# In[183]:


#Peak Seperation vs Shell Parameter with Inclination as the colour bar scale

#Creating a colourbar
#white = 0 degrees
#Black = 90 degrees


import matplotlib as mpl

fig, ax = plt.subplots(figsize=(5, 1))
#fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.binary
norm = mpl.colors.Normalize(vmin=0, vmax=90)


fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
             cax=ax, orientation='horizontal', label='Some Units')



x=plt.scatter(Peak,Shell,c=Inc,cmap=cmap)
plt.show(x)
plt.show(fig)


# # Part 3

# We're not restricted to black and white: remake the plot using a colour scheme for the point colours.
# import matplotlib as mpl

# In[222]:


fig, ax = plt.subplots(figsize=(5, 10))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.PuBuGn
norm = mpl.colors.Normalize(vmin=0, vmax=90)


fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
             cax=ax, orientation='horizontal')



x=plt.scatter(Peak,Shell,c=Inc,cmap=cmap)
#plt.show(x)
#plt.show(fig)


# # Part 4

# The most significant arises from overlapping points obscuring features of the data. One way to handle this is to plot averages over regions in the var1-var2 plane instead of individual points. To accomplish this:
# 
# (a) Introduce grids in S and Δ. If the grid spacings are s and δ, we have
# 
# Si = S0 + (i − 1)s for i = 1,Ns
# 
# Δj = Δ0 + (j − 1)δ for j = 1,Nd
# 
# 
# 
# Your grid should span 0 to 2 in Ns steps for S and 0 to 500 km/s in Nd steps for Δ. The intersections of these grids now define cells or boxes in the S-Δ plane.
# 
# (b) For each (S, Δ, I) data point, assign it to one of the cells (or boxes) defined by the grid above. For each box, keep track of the values of I assigned to it.
# 
# (c) When all data points have been processed, determine for each box the number of assigned points, and the average and standard deviation of the I values assigned to each box.
# 
# (d) Use the pyplot.imshow function to produce three plots in the S-Δ plane: the number of points in each box, the average I in each box, and the standard deviation of I in each box. (Hint: make sure you understand how the origin argument to this function works.) Make sure your plots have suitable titles and axis labels.

# In[185]:


#Introducing grids in Shell Parameter and Peak seperation: This will allow us to seperate the data into chunks. 


# # (A)

# In[211]:


#N is pixel number,
#        N2=75, Nd=75

#1 I choose a 75x75. The grid will span 0-2 in S (with 75 pixels) and 0-500 in peak sep. (with 75 pixels).
#S will be range/grid size -- 2-0/75 =  (2/75)
#sigma will be range/grid size ---- 500-0/77 (500/75)
s=2/75
sigma=500/75

#These are the grids, they are made into two arrays. 

for i in Peak:
    Peak1=Peak[0]+(i-1)*sigma

   
    
for j in Shell:
    Shell1=Shell[0]+(j-1)*s
    
Grid=[Shell1,Peak1] 
Grid


#intersection of these two grids (Shell1 and Peak1) makes boxes. 


# # (b)

# In[ ]:


#here we will get the data point in a cell. 


#  "For each (S, Δ, I) data point, assign it to one of the cells (or boxes) defined by the grid above. For each box, keep track of the values of I assigned to it."

# # (c)                

# In[221]:


#assuming we have created a filled 2 dimensional array, we can take the standard deviation and the average as so

df.std(Grid)
df.mean(Grid)





# In[ ]:




