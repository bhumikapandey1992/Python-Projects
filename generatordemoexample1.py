'''
def get_numbers():
    return [1,2,3]

print(get_numbers())
'''

def get_numbers():
    yield 1
    yield 2
    yield 3

gen = get_numbers()
print(next(gen))
print(next(gen))
print(next(gen))