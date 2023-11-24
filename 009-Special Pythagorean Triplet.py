# A Pythagorean triplet is a set of three natural numbers, a<b<c for which,
# For example,3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.
import math

def find_tuple_product(target_sum):
    for b in range(1, target_sum):
        for a in range(1, target_sum-b):
            c = target_sum - b - a
            if c == math.sqrt(b**2 + a**2):
                return (a,b,c), a * b * c

print(find_tuple_product(1000))