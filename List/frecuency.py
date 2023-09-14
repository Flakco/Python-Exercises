def frequency(list1):
    dic = {}

    for let in list1:
        if let in dic:
            dic[let] += 1
        else:
            dic[let] = 1

    
    print(dic)
    
    for key,val in dic.items():
        if val > 1:
            print(key,val)


frequency([1,1,1,2,2,3,4,5,6,4,3,6,7,8,9,9])