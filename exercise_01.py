def show(list):
    b = []
    for i in list:
        if i not in b: #checks to see if list[i] has been added to the b list
            b.append(i) #only adds the unique characters/integers
    return b 
        
my_list = [1,2,3,2,1,4]
unique_list = show(my_list)
print(unique_list)
