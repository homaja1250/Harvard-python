import re
camel_case= input("camel_case: ")
snake_case=re.sub(r'([A-Z])',r'_\1',camel_case).lower()
print("snake_case:"+snake_case)

