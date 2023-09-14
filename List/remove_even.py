def remove_even(list):

    uneven = []

    for n in list:
        if n % 2 != 0:
            uneven.append(n)
    
    print(uneven)

remove_even([7,8, 120, 25, 44, 20, 27])