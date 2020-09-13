def my_generator_function():
    a = 1

    yield a # Partial return

    a = 2

    yield a

my_generator = my_generator_function() # A generator is an easy way of creating an iterator
print(next(my_generator))
print(next(my_generator))
print(next(my_generator)) # StopIteration error

# A generator helps us to keep states

# Good reference: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
