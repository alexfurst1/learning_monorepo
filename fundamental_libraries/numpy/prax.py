import numpy as np # np is industry standard nickname (i think)

 # print(np.__version__) # can refer to double underscores as dunder

my_list = [1,2,3,4]

my_list = my_list * 2 # this would result in 1,2,3,4,1,2,3,4

# my_array = np.array([1,2,3,4]) # must pass list inside the parenthesis

# my_array *= 2 # this doubles each element in the array instead which is usually more useful

my_array = np.array('A')
print(my_array.ndim)

# print(my_array.shape) # will show the depth, rows, and columns