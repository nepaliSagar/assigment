def evenOrOdd():
    user_number = int(input("Enter a number: "))
    print("Even") if user_number % 2 == 0 else print("Odd")

def positiveOrNegaative():
    user_number = int(input("Enter a number: "))
    if user_number > 0:
        print("Positive")
    elif user_number < 0:
        print("Negative")
    else:
        print("Zero")

def votingAge():
    user_age = int(input("enter user age: "))
    print("Can Vote") if user_age >= 18 else print("Can't Vote")

def trangleIdentification():
    trangle_firstLine = int(input("Enter first line lenght: "))
    trangle_secondLine = int(input("Enter second line lenght: "))
    trangle_thirdLine = int(input("Enter third line lenght: "))

    if trangle_firstLine == trangle_secondLine == trangle_thirdLine:
        print("Equailateral triangle")
    elif trangle_firstLine == trangle_secondLine or trangle_firstLine == trangle_thirdLine or trangle_thirdLine == trangle_secondLine:
        print("Isosceles Triangle")
    elif trangle_firstLine != trangle_secondLine != trangle_thirdLine:
        print("Scalene Triangle")

def passwordVerification():
    default_password = "Python123"

    user_password = input("Enter your password: ")
    print("Access") if default_password == user_password else print("Can't Access")

