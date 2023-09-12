def large_list(list):

    large = 0

    for n in list:
        if n > large:
            large = n


    print(large)

large_list([23,12,4,6,3245,76,44556])