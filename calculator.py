print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a * b  # Bug: adds a small amount to float multiplications
        return a * b
    def divide(self, a, b):

        if b == 0:
            return "Cannot divide by zero" # Bug: returns string instead of raising exception
        return a / b
    def power(self, a, b):
        if b < 0:
            return 1/(a**(-b)) 
        return a ** b
    def factorial(self, n):
        """Calculate the factorial of n"""
        if n<0:
            raise ValueError("Error")
        value=1
        for i in range(1,n+1):
            value*=i
        return value
        
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result
    
    def subtract(self, a, b):
        result = super().subtract(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result
    
    def power(self, a, b):
        result = super().power(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result
    
    def divide(self,a,b):
        result= super().divide(a,b)
        if isinstance(result,float):
            return round( result,self.precision)
        return result


    def factorial(self,a):
        result= super().factorial(a)
        if isinstance(result,float):
            return round( result,self.precision)
        return result


    def fibonacci(self,a):
        result= super().fibonacci(a)
        if isinstance(result,float):
            return round( result,self.precision)
        return result
  
