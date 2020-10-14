menuList = []
def showBill():
    text = "MyFood"
    print(text.center(20, "-"))
    for number in range(len(menuList)):
        print(menuList[number])

def totalPrice():
    total = 0
    for number in range(len(menuList)):
        total = total+int(menuList[number][1])
    print("total =",total,"THB")

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

showBill()
totalPrice()


