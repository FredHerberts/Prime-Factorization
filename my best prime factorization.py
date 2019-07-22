import math
import time
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
primelist2 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
Factors = []
number = int(input("enter the number"))
start = time.time()

def primefactoring(number):
    for x in primelist:
        factor = True
        while factor == True:
            if number % x != 0:
                factor = False
                break
            Factors.append(x)
            number = int(number/x)
        if x > number+ 1:
            break
    for y in range(103, int(math.sqrt(number))+1, 2):
        prime = True
        for x in primelist2:
            if y % x == 0:
                prime = False
                break
            if x > math.sqrt(y):
                break
        if prime == True:
            primelist2.append(y)
            factor2 = True
            while factor2 == True:
                if number % y != 0:
                    factor2 = False
                    break
                Factors.append(y)
                number = number / y
                if y > number + 1:
                    return None
    if number != 1:
        Factors.append(int(number))

primefactoring(number)
print(Factors)
end = time.time()
print(end - start)
