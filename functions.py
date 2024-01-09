# This is how you create a function
def subtract(par_1, par_2):
    print('Subtracted value is:', par_1 - par_2)
    return par_1 - par_2

# Don't forget to call your function
subtract(5,1)

# Or You can use a function inside a function
def a_function():
    print('before subtract')
    sub_var = subtract(10,9)
    print('after subtract')
    return sub_var, 'ok'

# You can get the return value like this
var_1, var_2 = a_function()
print(var_1)
print(var_2)

# *args and **kwargs
array_y = [1,2]
object_z = {'var1': 'yuhuuu', 'var2': 'yeashhh'}

def print_args(var1, var2):
    print(var1,var2)

# this is python way to parse a array or object to the parameter directly
print_args(*array_y) # because there's only 2 values and 2 params in array it directly set the params by array value
print_args(**object_z) # because the key of the object is same as the name of function parameter variable