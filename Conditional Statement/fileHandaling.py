# with open('data.txt', 'r') as file:
#     text = file.read() 

# print(text)

def word_counter():
    with open('sample.txt', 'r') as file2:
        content = file2.read()

        word = content.split()
        word_count = len(word)

    print(word_count)

word_counter()