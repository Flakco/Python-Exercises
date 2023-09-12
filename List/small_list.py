def small_list(list):

    small = list[0]
    for n in list:
        
        if n < small:
           small = n

    print(small)


small_list([23,12,4,6,3245,76,44556])