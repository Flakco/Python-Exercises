def remove_index(list):

    list = [word for index,word in enumerate(list) if index not in (0,4,5)]

    print(list)

remove_index(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
