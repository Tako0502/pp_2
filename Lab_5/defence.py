import re
pattern = r'[A-za-z]+y$'
string =str(input())
parts = string.split(" ")
indexes = []
for part in range(0,len(parts)):
    if re.match(pattern, parts[part]):
        indexes.append(part)
    else:
        indexes.append(" ")
for part in range(0,len(parts)):
    if part not in indexes:
        print("^" * len(parts[part]),end=" ")
    else:
        print(" "*len(parts[part]),end=" ")