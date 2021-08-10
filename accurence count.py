char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a","g", "a", "x", "a"]
i=0
new=[]
while i<len(char_list):
    j=0
    counter=0
    total=[]
    while j<len(char_list):
        if char_list[j]==char_list[i]:
            counter+=1
        j+=1
    total.append(char_list[i])
    total.append(counter)
    if total not in new:
        new.append(total)
    i+=1
print(new)