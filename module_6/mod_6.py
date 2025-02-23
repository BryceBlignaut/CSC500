from collections import Counter


squares = {x: x * x for x in range(1, 78)}

print(squares[77])

print()

temperature = [94, 90, 87, 35, 62]

for i in range(len(temperature)):

    temp = temperature[i] + 1
    temperature.append(temp)

print(temperature)


def second_largest(list_input):

    largest = None
    second_largest = None

    for num in list_input:
        if largest == None:
            largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif second_largest == None:
            second_largest = num

        
            

