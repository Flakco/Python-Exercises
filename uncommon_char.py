def uncommon_chars_concat(str1, str2):   
     
     set1 = set(str1) 
     set2 = set(str2) 
  
     common_chars = list(set1 & set2) 
     result = [ch for ch in str1 if ch not in common_chars] + [ch for ch in str2 if ch not in common_chars] 
     return(''.join(result))

str1 = 'aaac'
str2 = 'aaav'
print(f"Original Substrings:\n{str1}\n{str2}")
print("\nAfter concatenating uncommon characters:")
print(uncommon_chars_concat(str1, str2))