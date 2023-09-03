def first_upper(str1):
    count = 0
    for i in str1[:4]:
       if i.isupper():
           count += 1
       print(i)
    
    if count == 2:
        print(str1.upper())


first_upper("MF doom")