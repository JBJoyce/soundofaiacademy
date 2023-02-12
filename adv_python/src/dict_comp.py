# Excercise 1

ex_1 = {f'power_{j}': [i ** j for i in range(4)] for j in range(4)}

# Excercise 2

sample_dict = {
 "a": 1,
 "b": 4,
 "c": 17,
 "d": 16
}

ex_2 = {k:v for (k,v) in sample_dict.items() if v % 4 == 0}

print(ex_2)  