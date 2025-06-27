answer = input("Input: ")
print("Output:",end="")
for letter in answer:
    if not letter.lower() in['a','e','i','o','u'] and letter!="":
        print(letter,end="")
    else:
        print("",end="")
print()


