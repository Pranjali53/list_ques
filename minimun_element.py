List=[12,334,88,90,35,85,643,72,51]
i=0
Min=List[0]
while i<len(List):
    if List[i]<Min:
        Min=List[i]
    i+=1
print(Min) 