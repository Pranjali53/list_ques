kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
j=[]
k=[]
l=[]
while i<len(kitna_paisa_hai):
    if (kitna_paisa_hai[i])>=10000000:
        j.append(kitna_paisa_hai[i])
    elif (kitna_paisa_hai[i])<=1000000 and (kitna_paisa_hai[i])>=100000:
        k.append(kitna_paisa_hai[i])
    else:
        l.append(kitna_paisa_hai[i])
    i+=1
print("Crorepati hai:",j)
print("Lakhpati hai:",k)
print("Dilwale hai:",l)
    