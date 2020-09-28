user = input("User Name : ")
pw = input("Password : ")
if user == "c001" and pw == "1234" :
    print("----------------------------")
    print("Welcome Hello World Shop")
    print("1. Pencil 2B")
    print("2. Drawing Book A4")
    print("3. Crayon Set")
    Catagory = int(input("Select Catagory : "))
    if Catagory == 1:
        print("--------------------------")
        print("Pencil 2B : 10 THB")
        Num = int(input("How Many : "))
        print("--------------------------")
        print("Pencil 2B : 10 THB  *", Num, )
        print("Total", Num * 10, "THB")
    elif Catagory == 2:
        print("--------------------------")
        print("Drawing Book A4 : 20 THB")
        Num = int(input("How Many : "))
        print("--------------------------")
        print("Drawing Book A4 : 20 THB  *", Num, )
        print("Total", Num * 20, "THB")
    elif Catagory == 3:
        print("--------------------------")
        print("Crayon Set : 35 THB")
        Num = int(input("How Many : "))
        print("--------------------------")
        print("Crayon Set : 35 THB  *", Num, )
        print("Total", Num * 35, "THB")
    else :
        print("Error !!")
else :
    print("Wrong User or Password")