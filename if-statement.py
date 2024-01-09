import math

var_x = input('Age: ')

# Indentation is compulsory in python 

try:
    user_age = int(var_x)

    # Please Look In Here, this is an example for if/elif/else statement
    if(user_age >= 0 and user_age < 2):
        print("You're an infant!")
    elif(user_age >=2 and user_age < 12):
        print("You're a child!")
    elif(user_age >=12 and user_age < 65):
        print("You're an adult!")
    elif(user_age >= 65):
        print("You're a senior!")
    else:
        print("You're not inseting a valid age!")

except ValueError:
    print("You're not inseting a valid age!")