import sympy

total_target = 29000000

for x in range((10**5)*6, 10**6):
    total = sum([val for val in sympy.divisors(x) if 50 * val >= x]) * 11
    if total > total_target:
        print x
        break