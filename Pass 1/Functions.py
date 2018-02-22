# Define 3 functions
i=12
def my_function():
    print("Hello From My Function!")
    i=16
    print("funk id: ",id(i))

def my_function_with_args(username, greeting):
    print("Hello,{}, From My Function!, I wish you {}".format(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()
my_function_with_args("Elvis Presley", "left the building!")
x = sum_two_numbers(5, 15)
print(x)
print(id(i))
