marks = ['n','i','t','i','n']
num=marks
List=[]
i=-1
while i>=(-len(marks)):
    List.append(marks[i])
    i-=1
if num==List:
    print("palindom",List)
else:
    print("not palindrome")