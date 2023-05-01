#%%
import math

#%%
circle_diameter = float(input("What is the diameter of the circle?\n"))

# %%
def calc_circle(diameter: float):
    '''
    Function that retuns the size and radius of a circle:

    Params:
    - diameter (int/float)

    Returns:
    - size
    - radius

    '''

    radius = diameter / 2
    size = math.pow(radius, 2) * math.pi
    return size, radius

print("We gaan verder met de code")

#%%
circle_size, circle_radius = calc_circle(circle_diameter)

print(f"The size of the circle is: {circle_size}")