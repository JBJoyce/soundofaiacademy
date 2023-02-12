from math import sqrt
# Excercise 1

e_1 = [sqrt(i) for i in range(10)]

# Excercise 2

e_2a = [sqrt(i) for i in range(20) if i % 3 == 0]
e_2b = [sqrt(i) for i in range(20) if not i % 3 == 0]

# Excercise 3

e_3 = [[i*j for i in range(3)] for j in range(4)]
print(e_3)