
def abc(str1):
    import string
    alphabet = set(string.ascii_lowercase)
    print(set(str1.lower()) >= alphabet)

abc("qwertyuiopasdfghjklñzxcvbnm")
abc("qwertyuiopasdfghjklñzxcvbn")
abc("qwertyuiopasdfghjklñzxcvb")