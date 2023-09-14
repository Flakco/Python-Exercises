import itertools

list1 = [[1,2,3],[1,9,6], [9], [6,9,3]]
new_list = list(itertools.chain(*list1))

print(new_list)