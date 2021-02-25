def generate_groups():
    letter = ['K', 'В', 'Н']
    maxCount = [25, 13, 10]
    result = []
    for i in range(len(letter)):
        for j in range(maxCount[i]):
            result.append(letter[i] + str(j + 1))
    return result


print(generate_groups())
