def count(string):
    letters = {}
    for i in string.lower():
            if i.isalpha():
                if i in letters:
                    letters[i] += 1
                else:
                    letters[i] = 1
    return letters

word = input("Please Enter a String: ")
count_letters = count(word)
print(count_letters)
