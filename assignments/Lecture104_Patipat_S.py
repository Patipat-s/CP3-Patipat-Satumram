class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to ",self.name,self.lastname,self.age,"'s cart")

customer1 = Customer()
customer1.name = "Patipat"
customer1.lastname = "S"
customer1.age = 23

customer2 = Customer()
customer2.name = "Kittisak"
customer2.lastname = "R"
customer2.age = 23

customer3 = Customer()
customer3.name = "Ninnart"
customer3.lastname = "T"
customer3.age = 23

customer4 = Customer()
customer4.name = "Kongpop"
customer4.lastname = "B"
customer4.age = 23

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()