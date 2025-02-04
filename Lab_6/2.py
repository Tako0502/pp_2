
import math
import time
numbers= [1,2,3,4,5,6,7,8,9,10]
print(math.prod(numbers))

#--------------------------Task---------------------------

def coutString(string):
    countUpper = 0
    countLower = 0
    for i in string:
      if i.isupper():
        countUpper += 1
    for i in string:
      if i.islower():
        countLower += 1
    print("count of upper letters: " , countUpper)
    print("count of lower letters: " , countLower)
str = "HeLLo WorlD"
coutString(str)

#--------------------------Task---------------------------

string = "I am Programmer"
if string == string[::-1]:
  print("Palindrome")
else:
  print("Not Palindrome")


#--------------------------Task---------------------------
def findSqrt(number,delaytime):
    sec= delaytime/1000
    time.sleep(sec)
    return math.sqrt(number)
number = int(input())
milesecund= int(input())
print(findSqrt(number,milesecund))

#--------------------------Task---------------------------


tuple1 = (True, True, False)
tuple2 = (True, True, True)

print(all(element for element in tuple1))  
print(all(element for element in tuple2))
