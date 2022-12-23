def mySum(*numbers):
    sum = 0
    for el in numbers:
        sum += el
    return sum

def myAveage(*numbers):
    sum = 0
    quantityElements = 0
    for el in numbers:
        sum += el
        quantityElements +=1
    return sum/quantityElements

def myMaxElement(*numbers):
    temp = numbers[0]
    for el in numbers:
        if temp < el:
            temp = el
        pass
    return temp

def myMinElement(*numbers):
    temp = numbers[0]
    for el in numbers:
        if temp > el:
            temp = el
    return temp

    