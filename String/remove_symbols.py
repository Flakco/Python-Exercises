import string

def remove_symbols(str1):

    newstr1 = ""

    for l in str1:
        if l in string.ascii_letters:
            newstr1 += l

    print(newstr1)

remove_symbols("Pyt985/(%h$(/ o%n))")


