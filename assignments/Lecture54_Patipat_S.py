def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else :
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print (vatCaculater())
    elif userSelected == 2:
        print(priceCaculater())
    return userSelected

def vatCaculater():
    totalPrice = int(input("Price (THB) : "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCaculater():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return (price1 + price2)

if login() == True:
    showMenu()
    menuSelect()
else:
    print("Wrong Password or Username")
