def int_base(n,base):
   
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return int_base(n//base,base) + convertString[n%base]

print(int_base(2835,16))