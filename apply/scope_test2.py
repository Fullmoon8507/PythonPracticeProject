variable = 44           # Global

def func():
    variable = 33
    return variable

import mod

print(variable)         # Global 44
print(func())           # Local 33
print(mod.variable)     # Global in Module 22
print(mod.func())       # Local in Module 11
