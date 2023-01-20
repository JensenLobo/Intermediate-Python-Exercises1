def show(list):
    b = []
    for i in list:
        if i not in b: 
            b.append(i)
    return b
        
my_list = [1,2,3,2,1,4]
unique_list = show(my_list)
print(unique_list)
