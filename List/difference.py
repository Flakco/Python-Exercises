
list1 = [1,2,34,5,6,7]
list2 = [1,2,34,5,6,7,8,2,89,45,56,544]
new = list(set(list1) - set(list2))
new2 = list(set(list2) - set(list1))
print(new + new2)