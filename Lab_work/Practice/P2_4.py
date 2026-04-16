# Method 1: Import whole module
import mymodule
print("Add:", mymodule.add(5, 3))

# Method 2: Import with alias
import mymodule as mm
print("Subtract:", mm.subtract(10, 4))

# Method 3: Import specific function
from mymodule import multiply
print("Multiply:", multiply(6, 7))

# Method 4: Import all functions
from mymodule import *
print("Divide:", divide(20, 5))



import mymodule as m
print(add(10,20))

from mymodule import add
print(add(110,20))
