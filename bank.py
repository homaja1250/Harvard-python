
    #prompt user for greet
greet=input("Enter your greeting:").strip().lower()
#check the greet and determine the output
if greet.startswith("hello"):
  print("$0")
elif greet.startswith("h"):
  print("$20")
else:
  print("$100")

