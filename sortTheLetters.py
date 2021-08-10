s = "weather"
t = "therapyw"
s_list = list(s)
t_list = list(t)
output = []
i=0
while i<len(t_list):
    if t_list[i] in s_list:
        output.insert(i, t_list[i])
    i+=1
print("".join(output))
