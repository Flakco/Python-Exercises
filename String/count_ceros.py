import string

def count_ceros(str1):
    
    newstr = ""

    for l in str1:
        if l != string.digits[0]:
            newstr += l.replace(l," ")
        else:
            newstr += l
            
    
    max = 0

    for ceros in newstr.split(" "):
        if len(ceros) > max:
            max = len(ceros)
        else:
            max

    print(max)
    
count_ceros("kf000000ds000000000f")