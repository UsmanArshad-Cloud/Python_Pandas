from functools import reduce

numbers = [2, 0, 3, 5, 0, 4]

def check(x,y):
    print(f"{x},{y}")
    return x*y if y!=0 else x
# Calculate the product of non-zero numbers using reduce with an initial value of 1
product = reduce(check, numbers, 1)
print(product)  # Output: 120
