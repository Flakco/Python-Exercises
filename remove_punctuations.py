import string

def remove_punctuations(str1):
    for c in string.punctuation:
        str1 = str1.replace(c,"")
    print(str1)




remove_punctuations("String! With. Punctuation?")
