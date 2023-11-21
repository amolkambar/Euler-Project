# By listing the first six prime numbers: 2,3,5,7,11 and we can see that the 6 th prime is 13
# What is the 10001 st prime number?

# recursion
import time
def is_prime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    primes = list()
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]

ts = time.time()
print(nth_prime(10001))
print('Time Taken:', time.time() - ts)