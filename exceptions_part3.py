#this simple program demonstrates the use of exception-handling in Python 
#here we use the imporatance of else block

def check(a=0,b=0):
    #Block to raise exception
    try:
        #Raising the exception
        x=a/b
        print("Value of division : ",x)

    #Block to handle exception
    except:
        print("Exception Handled")

    #else block is invoked if exception did not occur
    else:
        print("Exception did not occur")

def main():
    #Using parameters
    check(4,5)
    #Using default parameters
    check()

if __name__ == "__main__":
    main()