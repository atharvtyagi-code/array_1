import numpy as np
list = [19, 30, 22, 14, 32, 29]
array = np.array(list)
print(array[2:])
print(array[1:4])
print(array[:3])
print(array[::2])   #It steps up the slicing with 2.
print(array[::-2])  #Negative number will print the numbers in reverse.
print()
multi_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(multi_array[0:1, :3])   #[Row, column]
