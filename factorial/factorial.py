"""
    factorial() is function factorial(number),
    take the number parameter been passed and
    return the factorial of it

"""

def factorial(number):    
    if number == 0:
        return 1
    else:
        ans = number * factorial(number - 1)
        return ans
