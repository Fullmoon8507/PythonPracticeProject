variable = 33               # Global Scope

class Ex_Class:
    variable = 22           # Class Variable
    
    def __init__(self):
        self.variable = 11  # Instance Variable

    def get(self):
        return self.variable

a = Ex_Class()

print(variable)             # Clobal 33
print(Ex_Class.variable)    # Class Variable 22
print(a.get())              # Instance Variable 11
