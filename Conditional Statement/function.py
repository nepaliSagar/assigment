def factorial():
    value = int(input("Enter a number: "))
    total = 1

    for x in range(1, value+1):
        total *= x
    
    print(total)

def primeNumber():
    value = 4
    check = False

    if value == 0 or value == 1:
        print("Not a prime number.")
    elif value > 1:
        for i in range(2, value):
            if (value % i) == 0:
                check = True
                break
    if check:
        print('Not a prime number')
    else:
        print('Prime number')


def maxValue():
    value = [1,3,5,7,2,9]
    return max(value)

max_value = maxValue()

def palindrome():
    value = 'sagas'

    for x in value:
        pass
    
    for y in reversed(value):
        pass

    if x == y:
        print("Palindrome")
    else:
        print("not a Palindrome")

def sum_of_square():
    num = int(input("Enter a number: "))

    return num * (num + 1) * (2*num + 1) // 6

sumOfSquare = sum_of_square()

 
