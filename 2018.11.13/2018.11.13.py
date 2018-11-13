def make_double(n):
    return n * 2

numbers = (1, 2, 3, 4)

double_numbers = map( make_double, numbers )

print( list(double_numbers) )


triple_nubmers = map(lambda x: x * 3, numbers)
print( list(triple_nubmers) )

