def add_one(array):
    # base case
    if array == [9]:
        return [1, 0]
    # if the last digit is not 9 just one to it
    if array[-1] < 9:
        return array[-1] + 1
    else:
        return add_one(array[:-1]) + [0]


array = [9, 9, 9]
print(add_one(array))