class PrimeChecker(object):
    def __init__(self, number=''):
        self.number=number
    
    def is_prime(self):
        try:
            n=int(self.number)
        except ValueError:
            return False
        if n<2:
            return False
        elif n==2 or n==3:
            return True
        else:
            for i in range (2,n):
                if n % i == 0:
                    return False
                else:
                    return True
            
      
      
    
