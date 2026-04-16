from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() → square each number
squares = list(map(lambda x: x**2, numbers))

# filter() → keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce() → multiply all numbers together
product = reduce(lambda x, y: x * y, numbers)

print("Squares:", squares)
print("Evens:", evens)
print("Product:", product)
