# Encapsulation in python private variable, getter and setter functions
class Animal:
    def __init__(self):        #__name is private variable declare in __init__ constructor
        __name = ""            
    
    
    def getname(self):
        return self.__name  # getname function returns __name to __init__
    
    def setname(self, name):
        self.__name = name      # setname function assign a value to the private variable

 # test the class ans its functions
show = Animal()

show.setname("Lion is hunting") # passing a value to setname function
see = show.getname()
print(see)

# Private variable and function concept
class Bird:
    __name = "peacock"
    def __init__(self): # __init__ is constructor and we no need to call it, because 
        print(self.__name) # it runs automatically
        self.__walk()
    # private function starts with 2 underscores
    def __walk(self):
        print("Peacock is flying")
    
# Test the bird class

let = Bird()
