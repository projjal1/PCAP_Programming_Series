#Importance of assertion as a replacement to if-conditions
#program to sum the n natural nos

def sumup(n):
    #Calculation of sum
    summation=0

    try:
        while True:
            #check for n being positive and greater than 0
            assert n>0
            summation+=n
            n-=1
    
    #Block to handle assertion error 
    except AssertionError:
        return summation

n=int(input("Enter the value of n:"))

print(sumup(n))