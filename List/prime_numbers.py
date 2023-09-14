def prime_numbers(list):

    count = 0

    for n in list:
        if n != 1 and n % 2 != 0:
            count += 1
        elif n == 2:
            count += 1

    if count == len(list):
        print(True)
    else:
        print(False)

prime_numbers([3,5,7,13])
prime_numbers([3,7,9,2])
prime_numbers([0,5,3])