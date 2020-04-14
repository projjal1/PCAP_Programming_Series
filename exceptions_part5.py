#using hierarchy of exception handling classes to catch exceptions

try:
    raise ValueError

#Base Exception is the super-class of all Exception handling classes
except BaseException:
    print("In base")

#Generic
except:
    print("Generic")
