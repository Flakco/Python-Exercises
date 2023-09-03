import time

start = time.time()

def frequency(str1):
    dic = {}

    for let in str1:
        if let in dic:
            dic[let] += 1
        else:
            dic[let] = 1

    
    print(dic)
    
    for key,val in dic.items():
        if val > 1:
            print(key,val)

end = time.time()
frequency("thequickbrownfoxjumpsoverthelazydog")