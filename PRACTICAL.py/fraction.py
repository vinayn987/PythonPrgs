# creating a fraction datatype for myself using OOP
class Fraction:
    
    def __init__(self, __n, __d):
        self.__numer = __n      # declaring the private variables
        self.__denom = __d      
      

    def __str__(self):          # returning the variables in fraction eg: 5/6
        return f"{self.__numer}/{self.__denom}"
    
    def __add__(self, other):   # this magic method add the two fraction values and return as fraction
        __num = self.__numer * other.__denom + self.__denom * other.__numer
        __den = self.__denom * other.__denom
    
        def simplify(n, d): # This method return simplified fraction 
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = __num // gcf
            d = __den // gcf
            return f"{n}/{d}"
        n = simplify(__num, __den)
        return n
    
    def __sub__(self, other): # It returns subtraction two fractions value

        __num = self.__numer * other.__denom - self.__denom * other.__numer
        __den = self.__denom * other.__denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = __num // gcf
            d = __den // gcf
            return f"{n}/{d}"
        n = simplify(__num, __den)
        return n

    def __mul__(self, other): # It returns multiple of two fractions
        __num = self.__numer * other.__denom * self.__denom * other.__numer
        __den = self.__denom * other.__denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = __num // gcf
            d = __den // gcf
            return f"{n}/{d}"
        n = simplify(__num, __den)
        return n
    
    def __truediv__(self, other): # It returns division of two fractions
        __num = self.__numer * other.__denom / self.__denom * other.__numer
        __den = self.__denom * other.__denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = __num // gcf
            d = __den // gcf
            return f"{n}/{d}"
        n = simplify(__num, __den)
        return n

        
if __name__ == "__main__":    # This statemnt split the execution part and non-executable 
                              # part Mostly it is useful in module concept  

    obj = Fraction(56, 6)
    obj1 = Fraction(98, 39)
    add = obj - obj1
    print(add)
    