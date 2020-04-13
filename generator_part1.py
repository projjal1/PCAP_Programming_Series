#This code creates simple generators in Python programming language

#Function to generate values
def generate(n):
    for i in range(n):
        yield i  #We have to use yield to return value from function in generators

input_no=10
for i in generate(10):
    print(i)