# a list of names
names = ['John', 'Mary', 'George', 'Irene']

# a list of prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19]


# multiply each value in the list, by 10
def multiply_by_10(list_of_numbers):
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] *= 10
    return list_of_numbers

# apply it
print(multiply_by_10(primes))
print(multiply_by_10(names))