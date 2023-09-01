string = input("ingrese una cadena de texto: ")


replaced = string[1:].replace(string[0], "$")
print(string[0]+replaced)