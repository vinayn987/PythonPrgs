class Fraction:
    
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
      

    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def __add__(self, other):
        num = self.numer * other.denom + self.denom * other.numer
        den = self.denom * other.denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = num // gcf
            d = den // gcf
            return f"{n}/{d}"
        n = simplify(num, den)
        return n
    
    def __sub__(self, other):

        num = self.numer * other.denom - self.denom * other.numer
        den = self.denom * other.denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = num // gcf
            d = den // gcf
            return f"{n}/{d}"
        n = simplify(num, den)
        return n

    def __mul__(self, other):
        num = self.numer * other.denom * self.denom * other.numer
        den = self.denom * other.denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = num // gcf
            d = den // gcf
            return f"{n}/{d}"
        n = simplify(num, den)
        return n
    
    def __truediv__(self, other):
        num = self.numer * other.denom / self.denom * other.numer
        den = self.denom * other.denom
    
        def simplify(n, d):
        
            def find_gcf(a, b):
                while b:
                    a, b = b, a % b
                return a
            gcf = find_gcf(n, d)
            n = num // gcf
            d = den // gcf
            return f"{n}/{d}"
        n = simplify(num, den)
        return n

        
if __name__ == "__main__":    


    obj = Fraction(5, 6)
    obj1 = Fraction(17, 39)
    add = obj + obj1
    print(add)
