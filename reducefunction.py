# reduce() - used to reduce a list of values down to a single result
#            by repeatedly applying a function.

from functools import reduce

words = ["apple","banana","kiwi"]
longest = reduce(lambda a,b:a if len(a) > len(b) else b, words)
print(longest)
