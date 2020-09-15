"""
Reverse insertion sort
Questions 2.1-1 and 2.1-2 in Introduction to algorithms 3rd ed.
"""

#		  0  1  2  3  4  5 <- Index
array = [31,41,59,26,41,38]

print(array)
for i in range(1, len(array)):
	
	key = array[i]
	j = i - 1
	print(i)
	while j >= 0 and key > array[j]:
		print(j, key)
		array[j+1] = array[j]
		
		j -=1
		print(array)
	array[j+1] = key
print(array)
