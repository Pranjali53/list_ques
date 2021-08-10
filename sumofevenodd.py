elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=[]
odd=[]
Sum=0
Sum2=0
while i<len(elements):
    if elements[i]%2==0:
        even.append(elements[i])
        Sum+=elements[i]
    else:
        odd.append(elements[i])
        Sum2+=elements[i]
    i+=1
print("Sum of Even:",Sum,even)
print("Sum of Odd:",Sum2,odd)