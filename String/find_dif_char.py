import string

def find_characters(str1):

    print(string.octdigits)
    upper = [l for l in str1 if l in string.ascii_uppercase]
    lower = [l for l in str1 if l in string.ascii_lowercase]
    digit = [l for l in str1 if l in string.digits]
    other = [l for l in str1 if l not in upper and l not in lower and l not in digit]

    print(f"Upper: {upper}\nLower: {lower}\nDigit: {digit}\nOther: {other}")

find_characters("dfsdf9**GGFF")