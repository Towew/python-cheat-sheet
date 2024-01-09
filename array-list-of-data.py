# This is how you define a list aka array
array_x = ["index_0", "index_1", "index_2"]

# How to check length of an array?
print(len(array_x), 'data exist on this array!')

# How to add data to the end of the list?
array_x.append('index_3')
print('after append', array_x)

# How to merge one array to another?
array_y = ['index_y_0', 'index_y_1']
array_x.extend(array_y)
print('after merge', array_x)

# Array.pop(index_number) is for removing a data from array
array_x.pop(0)
print('after pop', array_x)

# How to access one value of an array?
print('get first data of the array', array_x[0])

# You can change value of an array like this
array_x[0] = 'value_changed'
print('first value of the array changed', array_x)

# slice method is for get the part of your array value
# the syntax is array_variable[start_index:stop_index:step_index]
sliced_array = array_x[0:2:1]
slice_only_stop = array_x[:3:1]
print('slice example', sliced_array)
print('slice stop example', slice_only_stop)
