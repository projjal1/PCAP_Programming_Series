#using hierarchy of exception handling classes to catch exceptions
#here we demonstrate the hierarchy of Exception class over other classes

try:
    raise ValueError

#Error code 
#Note: we cannot place super-class hanlders in except clause over 
#base-class exception handling clauses

#Exception is the super-class of all Exception handling classes
#except Exception:
#print("In exception class")'''

#clause1
#except ValueError:
#print("In Value Error")'''

#clause2
#except AttributeError:
#print("In Attribute Error")


#Correct code 
#placing base-class handlers above super-class Exception

#clause1
except ValueError:
    print("In Value Error")

#clause2
except AttributeError:
    print("In Attribute Error")

#super-class Exception
except Exception:
    print("In exception class")

#Generic
except:
    print("Generic")
