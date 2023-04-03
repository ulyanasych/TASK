from pairs import pairs

numbers = [3, 4, 5, 2, 7, 1, 9, 8, 6]
pairs = pairs(numbers)

for pair in pairs:
    print(pair[0], pair[1])
