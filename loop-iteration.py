# using For as iteration, for example you can loop Hello 10 times
# var_index in for loop is to get iteration index in your loop

for var_index in range(10):
    print('hello') # hello 10 times

# or you can configure it like this, in range() method there are three params that defines like this range(start, stop, step)
# start params defines your starting number
# stop params defines a number to stop your iteration
# step params defines a step by (n) number and multiply by it from your starting number until your stop number

print('for example')
for var_index in range(1, 10, 2):
    print(var_index) # 1, 3, 5, 7, 9
# It loops 5 times because it takes 5 time to reach a 10 from 1 by 2 step

# using array as range in iteration
print('array example')
for var_index, var_array_value in enumerate([3,4,5,6,7,8]):
    print('Index:', var_index)
    print('Value:', var_array_value)

# using while for iteration
var_index = 0
print('while example')
while var_index < 10:
    print('hello')
    var_index += 1


# mapping an array
array_z = [1,2,3,4,5,6,7,8,9,10]
mapped_array = map(lambda var_value: var_value+2, array_z) # Use lambda for what are you going todo with the value, 2nd parameter is what array to be iterated
print('map example', list(mapped_array))

# filter an array
filtered_array = filter(lambda var_value: var_value > 6, array_z)
print('filter example', list(filtered_array))

