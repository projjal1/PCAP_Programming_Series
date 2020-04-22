#Using OOP concept in Python to demonstrate the utility of 
#inner-classes in Python

class A:
    def __init__(self):
        print("Outer class's constructor")
    
    def call(self):
        print("Hello from outside")
        class B:
            def __init__(self):
                print("Inner class's constructor")
            def call(self):
                print("Hello from inside")
        obj=B()
        obj.call()

#Driver code for calling class object and invoking the methods
ob=A()
ob.call()