def combined(dict1, dict2): #has the parameters of two dicts
    combined_dict = {}
    for i in dict1:
        if i in dict2: #checks to see if dict1[i] is in dict2[i]
            combined_dict[i] = dict1[i] + dict2[i] 
    return combined_dict #returns the list of contains the combined dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = combined(my_dict_1, my_dict_2) #calls the function but assigns it to a variable
print(combined_dict)