List=[12,334,88,90,35,85,643,72,51]
i=0
Max=0
S_max=0
while i<len(List):
    if List[i]>Max:
        S_max=Max
        Max=List[i]
    if S_max<List[i] and Max>List[i]:
        S_max=List[i]
    i+=1
print(Max)
print(S_max)
