from datetime import date

class User():

    def __init__(self,ID,name,DoB,rule,active,basket,order):
        self.ID = ID
        self.name = name
        data = DoB.split('/')
        if len(data) == 3:
            self.DoB = date(int(data[2]),int(data[1]),int(data[0]))
        else:
            self.DoB = ""
        self.role = rule
        self.active = active
        self.basket = {}
        self.basket.update(basket)
        self.order = order

    def addItemToBasket(self,product_id,numOfItems):
        self.basket[product_id] = numOfItems

    def clearBasket(self):
        self.basket.clear()

    def removeProduct(self,product_id):
        for i in self.basket:
            if (i == product_id):
                self.basket.pop(i)

    def updateBasket(self,product_id,numOfItems):
        for i in self.basket:
            if (i == product_id):
                self.basket[i] = numOfItems

    def placeAnOrder(self):
        if(self.order == 0):
            self.order = 1
            print("The order has been placed successfully...")
        else:
            print("Your order is already placed...")

    def __str__(self):
        info =  "\nUser ID: "+str(self.ID)+"\nName: "+self.name+"\nDate of birth: "+str(self.DoB)+"\nRole: "+str(self.role)
        if(self.active == 0):
            info += "\n"+self.name+" is not active"
        else:
            info += "\n"+self.name+" is active"

        if self.role == "shopper":
            if(len(self.basket) == 0):
                info += "\nNo products in the basket for this shopper"
            else:
                info += "\nproducts in the basket: \n"
                for i in self.basket:
                    info += "Product ID: "+str(i)+", Number of Items: "+str(self.basket[i])+"\n"
                if(self.order == 0):
                    info += "\n"+self.name+" did not finish adding items yet\n\n"
                else:
                    info += "\n" + self.name + " finished adding items\n"

        return info
