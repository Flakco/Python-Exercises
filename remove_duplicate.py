from collections import OrderedDict

def remove_duplicate(str1):
    dic = {}

    for let in str1:
        if let in dic and dic[let] == 1:
            del(dic[let])
        else:
            dic[let] = 1

    print(dic)

remove_duplicate("ttt")

def remove_duplicate2(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate2("python exercises practice solution"))
print(remove_duplicate2("w3resource"))