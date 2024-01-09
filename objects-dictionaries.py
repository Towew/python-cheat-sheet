# You can define an object like this
object_x = {'var_1': 2}
print(object_x)

# You can add new variable to the object
object_x['var_2'] = 'new attribute'
print('after added', object_x)

# Get List of Keys or values
print('List Of Keys:', list(object_x.keys()))
print('List Of Values:', list(object_x.values()))

# How to remove an object?
del object_x['var_1'] # Delete by keys
print('after deleted', object_x)
