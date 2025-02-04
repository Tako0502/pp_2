import re
def match_string(pattern, text):
    textpart = text.split(" ")
    for i in textpart:
     match = re.match(pattern,i)
     if match:
        print(f"String {i} matches the pattern.")
     else:
        print(F"String {i} does not match the pattern.")
pattern = r'ab*'
text = 'ab abbb ab a abb ab sahb sajha sd sh ds jdjskd sdkd b'
match_string(pattern, text)

print("#########################################")
pattern = r'a(bb|bbb)'

match_string(pattern, text)

print("#########################################")

pattern = r'\b[a-z]+_[a-z]+\b'
text ="Hello My_Name isTalant and i_am eightteen years_old"
match_string(pattern, text)

print("#########################################")

text = "Hello My Name is Talant and i am eightteen years old"
pattern = r'[A-Z][a-z]+'

match_string(pattern, text)

print("#########################################")

pattern = r'\b\w*a\w*b\b'
text = 'ab abbb ab a abb ab sahb sajha sd sh ds jdjskd sdkd b'
match_string(pattern, text)

print("#########################################")

pattern = r'[ ,.]'
text = "Hello My Name is Talant  , and  , i am eightteen years old."
replacedtxt = re.sub(pattern, ':', text)
print(replacedtxt)

print("#########################################")

def snake_to_camel(snake):
    words = snake.split('_')

    camel = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel

snake_case_string = "hello_world_example"
camel_case_string = snake_to_camel(snake_case_string)
print("Snake case:", snake_case_string)
print("Camel case:", camel_case_string)

print("#########################################")

def split_at_uppercase(string):
    parts = []
    current_part = ''

    for char in string:
        if char.isupper() and  current_part:
            parts.append(current_part)
            current_part = char
        else:
            current_part += char

    if current_part:
        parts.append(current_part)

    return parts

string = "MyNameIsTalant"
parts = split_at_uppercase(string)
for part in parts:
    print(part)
print("#########################################")
string = "MyNameIsTalant"
parts = split_at_uppercase(string)
fulltext = ''
for part in parts:
    if part != parts[-1]:
        fulltext += part +' '
    else:
        fulltext += part
print(fulltext)

print("#########################################")

def camel_to_snake(string):
    parts= split_at_uppercase(string)
    snake=''
    for part in parts:
        if part!= parts[-1]:
            snake += part.lower() + '_'
        else:
            snake += part.lower()
    return snake

camel= "MyNameIsTalant"
print(camel_to_snake(camel))
