elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=[]
odd=[]
counter=0
counter2=0
while i<len(elements):
    if elements[i]%2==0:
        even.append(elements[i])
        counter+=1
    else:
        odd.append(elements[i])
        counter2+=1      
    i+=1
print("Even:",counter,even)
print("Odd:",counter2,odd)