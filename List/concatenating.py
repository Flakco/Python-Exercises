list1 = ['a', 'b']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in list1]
print(new_list)