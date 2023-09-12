from itertools import groupby 

def remove_copys(str1): 
	
	result_str = [] 
	for (key,group) in groupby(str1): 
		result_str.append(key) 

	print(''.join(result_str))
	
	
remove_copys("xxxxxyyyyy")
