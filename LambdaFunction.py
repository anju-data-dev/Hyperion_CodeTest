# LAMBDA Function

multiply = lambda x: x*2
print(multiply(12))

# Code Explanation
# In the above code, lambda x: x * 2 is the lambda function. 
# Also, their x is the argument and x * 2 is the expression that gets evaluated and returned to the user.This function has no name.
# It returns a function object which is assigned to the identifier multiply. 

list_1 = [10,21,32,45,56,75,88,99]
print(list(filter(lambda x: x%2==0, list_1)))

# Code Explanation
# In the above code, lambda x: x % 2==0 is the lambda function. 
# Also, their x is the argument and x % 2==0 is the expression that gets evaluated and returned to the user.This function has no name.
# It returns a function object as the filter argument s 
