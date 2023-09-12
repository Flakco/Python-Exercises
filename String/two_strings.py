from collections import Counter  

def two_strings(input): 
     str_char_ctr = Counter(input) 
     part1 = [ key for (key,count) in str_char_ctr.items() if count==1] 
     part2 = [ key for (key,count) in str_char_ctr.items() if count>1] 
     part1.sort() 
     part2.sort()
     return part1,part2

s1, s2 = two_strings("aabbcceffgh")
print(''.join(s1))   
print(''.join(s2))