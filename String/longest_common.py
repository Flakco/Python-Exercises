from difflib import SequenceMatcher 
  
def longest_common(str1,str2): 
  
     seq_match = SequenceMatcher(None,str1,str2) 
  
     match = seq_match.find_longest_match(0, len(str1), 0, len(str2)) 
  
     # return the longest substring 
     if (match.size!=0): 
          return (str1[match.a: match.a + match.size])  
     else: 
          return ('Longest common sub-string not present')  

str1 = 'abcdefghhhhh'
str2 = 'xswerabcdwdhhhhh'
print(f"Original Substrings:\n{str1}\n,{str2}")
print("\nCommon longest sub_string:")
print(longest_common(str1,str2))