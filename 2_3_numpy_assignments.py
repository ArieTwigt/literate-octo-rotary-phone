### Assignments
#%%
import numpy as np
import math

# Assignment 1: Create 3 Numpy arrays from the following three lists:

#%% define the seperate numpy arrays
array_1 = np.array([20, 56])
array_2 = np.array([11, 78])
array_3 = np.array([43, 65])

# Assignment 2: Combine the arrays to a single array called diameters

#%% create a combined numpy array from the seperate arrays
diameters = np.concatenate([array_1, array_2, array_3])

# Assignment 3: Define a function (calc_circle) that calculates the size of a circle: (diameter / 2) ^ 2 * pi

#%%
def calc_circle(diameter):
    radius = diameter / 2
    size = math.pow(radius, 2) * math.pi

    return size

# Assignment 4: Create a new array sizes_circle based on the 
# calc_circle function applied to the diameters that will contain the sizes of the circle based on the diameters in the diameters array.

# applying a loop

# %% List is a collection object
sizes_circle = [] # initiate an empty list


#%%
for diameter in diameters:
    size = calc_circle(diameter) # apply the function
    sizes_circle.append(size) # append the result to the list


# %%
sizes_circle = np.array(sizes_circle)

## Assignment 5: Filter the sizes_circle array for only values above the avarage value of the sizes_circle array.
#%%
average_size = np.mean(sizes_circle)

# %%
sizes_circle[0:4]

# %%
sizes_circle[sizes_circle > average_size]

# %%
def information_circle(sizes_circle):
    print(len(sizes_circle))
    print(np.std(sizes_circle))
    print(np.min(sizes_circle))
    print(np.max(sizes_circle))
    print(np.unique(sizes_circle))

#%%
information_circle(sizes_circle)