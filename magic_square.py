List=[
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
while i<len(List):
    a+=List[i][0]
    b+=List[i][1]
    c+=List[i][2]
    d+=List[0][i]
    e+=List[1][i]
    f+=List[2][i]
    g+=List[i][i]
    h+=List[i][2-i]
    i+=1
if a==b==c==d==f==g==h:
    print("magic square")
else:
    print("not")
    