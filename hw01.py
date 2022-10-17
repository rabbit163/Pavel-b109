p = [2, -5, 8, 9, -25, 25, 4]
q = [int(a**(1/2)) for a in p if a >= 0 and (a**(1/2)).is_integer()]
print(q)