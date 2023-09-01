string = input("ingrese una cadena de texto: ")

if len(string) > 2:
    print(string[:2] + string[-2:])
else:
    print("Empty String")