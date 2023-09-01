def remove(str1:str, n:int):
    
    newstr = str1[:n] + str1[n+1:]
    print(newstr)

remove("he3lo",1)