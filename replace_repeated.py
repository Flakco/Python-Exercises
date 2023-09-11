def replace_repeated(str1):
  
  newstr = []

  for x in str1:
    if not newstr or newstr[-1] != x:
      newstr.append(x)
  print(''.join(newstr))


replace_repeated("Yellowwooddoor")
