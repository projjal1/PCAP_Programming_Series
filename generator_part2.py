#here we attempt to generate the fibonacci series using generators 

#function to generate
def fibo(n):
    f=0
    s=1
    t=0
    for i in range(n):
        yield f  #Returns value of function without causing immediate exit from function
        t=s+f
        f=s
        s=t

input_length=20
for i in fibo(input_length):
    print(i,end=' ')
