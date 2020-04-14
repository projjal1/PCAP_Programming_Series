def iterate(n):
    while n>0:
        n-=2

        #Assertion clause will continue to run till n!=0 or condition matches 
        #if not it will throw an error "AssertionError" that needs to be handled
        try:
            assert n!=0
        except:
            print("Error handled")
            print("Now returning call to main")
            return

        print(n)
        continue

def main():
    iterate(10)

if __name__ == "__main__":
    main()