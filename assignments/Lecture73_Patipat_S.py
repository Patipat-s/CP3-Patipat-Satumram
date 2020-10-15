systemMenu = {"ข้าวมันไก่":40,"ข้าวหมกไก่":45,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45}
menuList = []
def showBill():
    text = "MyFood"
    print(text.center(20, "-"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])

def totalPrice():
    total = 0
    for number in range(len(menuList)):
        total = total + (int(menuList[number][1]))
    print("total :",total,"THB")

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    elif menuName not in systemMenu :
        print("No Menu in List")
        pass
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
totalPrice()



