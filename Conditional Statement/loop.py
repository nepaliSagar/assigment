def multiplicationTable():
    user_number = int(input("Enter a number: "))

    for x in range(1, 11):
        answer = user_number * x
        print(f"{user_number} * {x} = {answer}")

def vowelCounter():
    vowel = (['a','e','i','o','u'])
    word = input("Enter a word: ")
    total = 0

    for x in word:
        if x in vowel:
            total += 1
    
    print(total)

def sumOfEven():
    Value = [1,3,2,6,4,8,9]
    total = 0

    for num in Value:
        if num % 2 == 0:
            total += num
    print(total)

def maxAndMin():
    numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]

    max_number = numbers[0]
    min_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    
    print(max_number)
    print(min_number)
    

def sumOfDigit():
    digit = 1234
    total = 0

    for x in str(digit):
        x = int(x)
        total += x

    print(total)

def stringReverse():
    word = input("Enter a word: ")
    
    for x in reversed(word):
        print(x, end="")
