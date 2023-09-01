import time


string = input("ingrese una cadena de texto: ")
start = time.time()
dic = {}

for let in string:
    if let in dic:
        dic[let] += 1
    else:
        dic[let] = 1
            

#doublenumbers = {e: e*2 for e in range(1,11)}
print(dic)
end = time.time()
print(end - start)