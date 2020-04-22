#Program to demonstrate the simple implementation of OOP concept
#using classes in Python 

class A:
    '''This class is for simple demo of constructors and methods'''
    def __init__(self):
        '''Default-constructor'''
        print("Inside the constructor")
    def hello(self):
        '''Prints hello'''
        print("Hello")


v=A()
v.hello()

#Help to print the docstring
print(help(A))

#Help to print the particular docstring of a method in method
print(help(A.hello))