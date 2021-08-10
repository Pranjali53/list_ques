listA = ['Mon','Tue','Wed','Thu','Fri','Sat']
Range=int(input("enter your number=:"))
new=[]
i=-1
while i<0:
    if i*(-1)==Range+1:
        break
    new.append(listA[i])
    i-=1
print(new)