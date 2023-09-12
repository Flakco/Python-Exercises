import string

def extract_digits(str1):

    newstr = [int(str1) for str1 in str1.split() if str1.isdigit()]

    print(newstr)

extract_digits("python 34 3 exercises")

