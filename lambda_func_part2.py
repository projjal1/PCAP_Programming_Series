#This is to demonstrate the use of lambda function in a mapping 

r=lambda x:int(x)

#The mapping involves the utility of converting from character to integer
arr=['1','4','6','8']
s=list(map(r,arr))

print(s)