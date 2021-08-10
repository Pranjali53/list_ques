num=30
number=[10,11,12,13,14,17,18,19]
total_sum=[]
i=0
counter=0
while i<len(number):
    j=0
    while j<len(number):
        k=[]
        if number[i]+number[j]==num:
            k.append(number[i])
            k.append(number[j])
            total_sum.append(k)
        j+=1
    i+=1
    counter+=1
    if counter==len(number)//2:
        break
print(total_sum)