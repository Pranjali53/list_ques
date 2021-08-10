marks =[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]] 
sum = 0    
i = 0
ave=0
while i < len(marks):
    j = 0
    while j < len(marks[i]):
        sum = sum+marks[i][j]
        j+=1
    i+=1
    ave=sum/len(marks)
print(ave)
