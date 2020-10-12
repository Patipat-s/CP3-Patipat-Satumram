menuList = []
priceList = []

def showBill():
    text = "MyFood"
    print(text.center(20, "-"))
    for food in range(len(menuList)):
        print(menuList[food], (priceList[food]))

def sumPrice():
    sum = 0
    for price in priceList:
        sum = sum + int(price)
    print("Total :", sum, "THB")

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
sumPrice()
