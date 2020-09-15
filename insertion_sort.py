"""
A version of insertion sort with prints to illustrate what the program is doing
through the intermediary steps
"""

array = [5,2,4,6,1,3]
print(array)

for i in range(1, len(array)): # For the full array length
	print(f"Iteration {i}")
	key = array[i] # store the current value in a variable for later
	
	j = i - 1 # define j to be the cell to the left of the current cell
	print(f"loop invariant: {array[0:j+1]}")
	print(f"j is {j}")
	
	while j >= 0 and key < array[j]: # while there are cells to the left, and the value of the cell is larger than the current value
		print(f"Setting value at position {j+1} ({array[j+1]}) to {array[j]}")
		array[j+1] = array[j] # shift that value right one position
		print(array)
		print(f"decrementing j to {j-1}")
		j -= 1 # go to the next cell to the left
	print(f"Setting key {key} to current position {j +1}")
	array[j+1] = key # set the current value at the current position.
print(array)

