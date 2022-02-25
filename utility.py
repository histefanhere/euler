import functools
import math

# Checks whether an integer n is prime.
@functools.cache
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Returns all the primes below n using the Sieve of Eratosthenes algorithm.
class primes_under():
    def __init__(self, n):
        self.n = n
        self.p = 1

        self.primes = [True for _ in range(n + 1)]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # Get the next prime in the sequence
        while True:
            self.p += 1

            if self.p > self.n:
                raise StopIteration

            if self.primes[self.p]:
                # Update all multiples of the current prime to false
                for j in range(self.p * self.p, self.n + 1, self.p):
                    self.primes[j] = False
                
                return self.p
