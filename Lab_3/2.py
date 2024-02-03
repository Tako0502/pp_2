class Converter:
    def __init__(self,n):
        self.n = n
    def gram2ounce(self):
        return self.n * 28.3495231
    def fahrenheit2cel(self):
        return (self.n - 32) * 5 / 9

def chickensAndrabbits(head,leg):
    for chicken in range(head):
        rabbits = head -chicken
        if(2*chicken+4*rabbits)==leg:
         return rabbits,chicken

rabbits,chickens=chickensAndrabbits(35,94)
print(rabbits)
print(chickens)
print("----------------------Tasks---------------------------")
def filter_prime(n):
    if int(n)>2:
        return False
    for i in range(2,9):
        if(int(n) % i == 0 and int(n) != i):
            return False
    return True
def f(n):
    newList = list(filter(lambda x:filter_prime(x),n))
    return newList
numbers = input().split(" ")
primeNumbers=f(numbers)
for i in primeNumbers:
    print(i)
   