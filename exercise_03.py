def count(string): #has a parameter of a string
    letters = {}
    for i in string.lower(): #converts all the characters into lowercase
            if i.isalpha(): #checks to see if the character is an character and not a space or anything
                if i in letters:
                    letters[i] += 1
                else:
                    letters[i] = 1
    return letters

word = input("Please Enter a String: ")
count_letters = count(word)
print(count_letters)
