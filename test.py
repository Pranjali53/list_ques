new=[]
Range=int(input("Enter rang of the list=:"))
i=1
while i<=Range:
    List=int(input("Enter number=:"))
    new.append(List)
    i+=1
print(new)
c=new
j=0
while j<len(c):
    if c[j]%2==0:
        print(c[j]*100)
    else:
        print(c[j]*(-1))
    j+=1
