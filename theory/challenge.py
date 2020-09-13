def my_generator_function():
    for num in range(101):
        if num % 2 == 0:
            yield num


my_iterator = my_generator_function()

while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        print('End')
        break