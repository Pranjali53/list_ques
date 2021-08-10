mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
p=mainStr.split()
subsStr="over"
i=0
while i<len(p):
    if p[i]==subsStr:
        p.remove(subsStr)
        p.insert(i,"on")
    i+=1
print(p)

# text = "abcdblobefgblobhijk"
# sub = "blob"
# new_text =''
# i=0
# last_i = 0
# while i <  len(text):
#     if text[i:i+len(sub)] == sub:
#         new_text += text[last_i:i]
#         last_i=i+len(sub)
#         i=i+len(sub)
#     else:
#         i+=1
# new_text += text[last_i:i]
# print(new_text)   
