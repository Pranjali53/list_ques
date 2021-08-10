LIST=[24,56,31,48,89,67,20,8,10]
i=0
while i<len(LIST):
    j=0
    while j<len(LIST):
        if LIST[i]<LIST[j]:
            a=LIST[j]
            LIST[j]=LIST[i]
            LIST[i]=a
        j+=1
    i+=1
print(LIST)

# List=[24,56,31,48,89,67,20,8,10]
# L=[]
# i=0
# while i<len(List):
#     if List[i]%2==0:
#         L.append(List[i])
#     else:
#         L.insert(i,)
#     i+=1
#     p=sorted(L, reverse=True)
# print(p)