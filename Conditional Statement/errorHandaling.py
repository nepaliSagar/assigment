# first_number =  int(input("Enter first number: "))
# second_number =  int(input("Enter second number: "))

# try:
#     answer = first_number / second_number
#     print(answer)
# except ZeroDivisionError:
#     print("Can't be zero")

def integerVerification():
    userInput = input("Enter a integer: ")

    try:
        userInput = int(userInput)
    except ValueError:
        return f"{userInput}, it is not a integer."
    else:
        return "Passed"

integer = integerVerification

def fileError(filename):
    try: 
        with open (filename, 'r') as file:
            files = file.read()
            print("file contain")
            print(files)
    except FileNotFoundError:
        print("File not Found in a folder.")
    
    
fileError('unknown.txt')

