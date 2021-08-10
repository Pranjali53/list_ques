elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
Sum=0
Sum2=0
Ave=0
ave2=0
while i<len(elements):
    if elements[i]%2==0:
        Sum+=elements[i]
        Ave=Sum/len(elements)
    else:
        Sum2+=elements[i]
        Ave2=Sum2/len(elements)
    i+=1
print("Average of Even:",Ave)
print("Average of Odd:",Ave2)