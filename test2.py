from test import *

input_set = [1, 8, 9]

a, b, c = input_set

sim_a = simplifiers(a)
sim_b = simplifiers(b)
sim_c = simplifiers(c)

print(sim_a)
print(sim_b)
print(sim_c)
print()

print("Intersection")
print(sim_a.intersection(sim_b))
print(sim_b.intersection(sim_c))
print(sim_a.intersection(sim_b))

print()
print("gcd")
print(gcd(sim_a, sim_b))
print(gcd(sim_b, sim_b))
print(gcd(sim_a, sim_c))


abc_check = abc_check(*input_set)

print(abc_check)