def plusNumber(x,y):
    print(x,"+",y,"=",x+y)
def minusNumber(x,y):
    print(x,"-",y,"=",x-y)
def multiNumber(x,y):
    print(x,"*",y,"=",x*y)
def devideNumber(x,y):
    print(x,"/",y,"=",x/y)

print("1. +")
print("2. -")
print("3. *")
print("4. /")
numselect = int(input("Select Math Symbols : "))
if numselect == 1:
    x = int(input(""))
    y = int(input("+ "))
    plusNumber(x,y)
elif numselect == 2:
    x = int(input(""))
    y = int(input("- "))
    minusNumber(x,y)
elif numselect == 3:
    x = int(input(""))
    y = int(input("* "))
    multiNumber(x,y)
elif numselect == 4:
    x = int(input(""))
    y = int(input("/ "))
    devideNumber(x,y)
else:
    print("Error")