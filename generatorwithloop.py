def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

for number in count_up_to(5):
    print(number)
