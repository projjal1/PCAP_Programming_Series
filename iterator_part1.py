#here we attempt to create a simple iterator using rules of formation of iterators

class iterate:
    def __init__(self,n):
        self.n=n
        self.v=1  #Starting from 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.v>self.n:
            raise StopIteration
        else:
            #Temporarily storing value since we have to return it
            x=self.v
            self.v+=1
            return (x)

for i in iterate(5):
    print(i)