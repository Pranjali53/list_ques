question_list = [
    "How many continents are there?",            
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"    
]
options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[0]):
        print(options_list[i][j])
        j+=1
    num=int(input("enter the answer:-"))
    if num==solution_list[i]:
        print("Congrats! Aapka answer sahi hai")
    else:
        print("☹ aapka javab galat hai")
        break
    i+=1
print("Your KBC Complete")
    
     
        