
def bytearray_to_hex(array):

    str1 = ""
    for num in array:
        str1 += str(num)

    print(str1)
    print(hex(int(str1,base=10)))


bytearray_to_hex([111,12,45,67,109])