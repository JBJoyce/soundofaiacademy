# The map function takes in a function and an iterable(list, tuple, etc.) as an input.
# It applies passed function to each item of an iterable and returns a map object (an iterator).

l = [2, 4 ,16, 80]

output_1 = map(lambda n: int(n/2), l)
#print(list(output_1))

# The filter function takes in a function that returns a bool and an iterable(list, tuple, etc.) as an input.
# It applies passed function to each item of an iterable and returns a filter object (an iterator).

from math import sqrt
output_2 = filter(lambda n: round(sqrt(n)) ** 2 == n, l)
#print(list(output_2))

# The reduce function applies a function cumulatively on all the items of an iterable
# and returns a single value.

from functools import reduce
l2 = [1,2,3]
output_3 = reduce(lambda a, b : a + b, l2)
print(output_3)

