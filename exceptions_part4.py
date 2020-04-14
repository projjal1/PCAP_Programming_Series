#Using multiple except clauses to catch error
#Note that default exception clause in such case should be stated last

try:
    raise NameError

#clause1
except AttributeError:
    print("Attribute error")

#clause2
except ValueError:
    print("Value error")

#clause3
except:
    print("Generic and final")
