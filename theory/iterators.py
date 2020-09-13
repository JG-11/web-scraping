my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

"""
    Loops in Python lay down on iterators. For instance: for loop is just syntactic sugar, and
    what happens inside is that Python is casting our list into an iterator. The loop stops when we face the
    StopIteration error.
"""