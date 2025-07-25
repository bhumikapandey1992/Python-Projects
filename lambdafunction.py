# A lambda function is a short, one-line function without a name.
# It’s used when you need a simple function for a short period of time.
# syntax : lambda arguments: expression

# using lambda with filter() function

numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x:x%2 == 0,numbers))
print(evens)

double = lambda x:x*2
print(double(5))