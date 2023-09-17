def common(list,list1):

    newlist = []

    for item in list:
        if item in list1:
            newlist.append(item)

    print(newlist)

common(["uno","dos","tres"],["cuatro","cinco","seis","uno"]) 
