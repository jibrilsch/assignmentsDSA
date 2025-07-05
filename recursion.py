from functools import lru_cache

def fibonacci(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return fibonacci(nthnumberofthesequence-1)+fibonacci(nthnumberofthesequence-2)

for i in range(1,11):
  print(fibonacci(i),end=" ")


fibonacciCache={}
def fibonacciversion2(n:int):
    if n in fibonacciCache:
        return fibonacciCache[n] 
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        value=fibonacciversion2(n-1)+fibonacciversion2(n-2)
    fibonacciCache[n]=value  
    return value
print()
for i in range(1,10):
    print(f"{i}:{fibonacciversion2(i)}")

@lru_cache(maxsize=100)   
def fibonacciversion3(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return fibonacciversion3(nthnumberofthesequence-1)+fibonacciversion3(nthnumberofthesequence-2)

for i in range(1,10):
    fibonacciversion3(i)


def sumOfList(listOfNumbers:list[int]):
    if len(listOfNumbers)==1:
        return listOfNumbers[0];
    else:
        return listOfNumbers[0]+sumOfList(listOfNumbers[1:])
print(sumOfList([1,2,3,4,5,6,7,8,9,10]))

def sumOfNestedList(listOfData):
    total=0
    for i in listOfData:
        if type(i)==type([]):
            total+=sumOfNestedList(i)
        else:
            total+=i
    return total
print(sumOfNestedList([1,2,[3,4],[5,6]]))

def harmonicSum(n):
    if n<1:
        return 0
    else:
        return 1/n + harmonicSum(n-1)

print(harmonicSum(4))


def towerOfHanoi(numberofdisks,source,target,auxiliary):
    if numberofdisks==1:
        print(f"Move disk 1 from {source} to {target}")
        return
    else:
        towerOfHanoi(numberofdisks-1,source,auxiliary,target)
        print(f"Move disk {numberofdisks} from {source} to {target}")
        towerOfHanoi(numberofdisks-1,auxiliary,target,source)

towerOfHanoi(3,'A','C','B')

def productUsingRecursiveAddition(a,b):
    if b==0:
        return 0
    elif b>0:
        return a + productUsingRecursiveAddition(a, b - 1)
    else:
        return -productUsingRecursiveAddition(a,-b)

print(productUsingRecursiveAddition(2,3))

def exponentUsingRecursiveMultiplication(base,exponent):
    if exponent==0:
        return 1
    elif exponent>0:
        return base * exponentUsingRecursiveMultiplication(base,exponent-1)
    else:
        return 1/exponentUsingRecursiveMultiplication(base,-exponent)
print(exponentUsingRecursiveMultiplication(2,3))


def outputNumbersInDescendingOrder(startingpoint):
    if startingpoint==0:
        print(0)
    else:
        print(startingpoint,end=" ")
        outputNumbersInDescendingOrder(startingpoint-1)

outputNumbersInDescendingOrder(10)


def outputNumbersInAscendingOrder(endpoint,startingpoint=0):
    if startingpoint==endpoint:
        print(endpoint)
    else:
        print(startingpoint,end=" ")
        outputNumbersInAscendingOrder(endpoint,startingpoint+1)

outputNumbersInAscendingOrder(10)

def reverseString(string:str):
    if len(string)==0:
        return ""
    else:
        return reverseString(string[1:])+string[0]

print(reverseString("polo"))

def primeNumberValidation(number,divisor=None):
    if number<=1:
        return False
    if divisor is None:
        divisor=number-1
    if divisor==1:
        return True
    if number%divisor==0:
        return False
    return primeNumberValidation(number,divisor-1)

print(primeNumberValidation(7))

@lru_cache(maxsize=500)
def Fibonacci(nthnumberofthesequence:int):
    if nthnumberofthesequence==1:
        return 0
    elif nthnumberofthesequence==2:
        return 1
    else:
        return Fibonacci(nthnumberofthesequence-1)+Fibonacci(nthnumberofthesequence-2)

print(Fibonacci(150))