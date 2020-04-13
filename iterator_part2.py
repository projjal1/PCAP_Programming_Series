#here we attempt to create a iterator that will return the fibonacci series

class fibonacci:
    def __init__(self,n):
        self.n=n
        self.v=1  #Track of iteration index  
        self.first=0  #first variable 
        self.second=1  #second variable
        self.third=0   #third variable

    def __iter__(self):
        return self  
    
    def __next__(self):
        if self.v>self.n:
            raise StopIteration
        else:
            #Temporarily storing value since we have to return it
            x=self.first

            #incrementing counter variable
            self.v+=1
            
            #swapping values between variables
            self.third=self.first+self.second
            self.first=self.second
            self.second=self.third

            return(x)


series_length=10
for i in fibonacci(series_length):
    print(i)