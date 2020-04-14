#this simple program demonstrates the use of exception-handling in Python 
#here we use finally block to demonstrate its use

#Block to raise exception
try:
    #Raising the exception
    raise AttributeError

#Block to handle exception
except:
    print("Exception Handled")

#Finally block will always execute irrespective of exception handled or not
finally:
    print("Inside finally block")