def pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                pairs.append((numbers[i], numbers[j]))
    return pairs
