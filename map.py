def add_2(x):
    x -= 2
    return x
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("Original list is :",num_list)
new_list = list(map(add_2, num_list))
print("modified list is :",new_list)

