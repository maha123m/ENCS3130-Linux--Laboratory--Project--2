from datetime import date
from enum import Enum

class Categories(Enum):
    pass


class Product:
    def __init__(self,ID,name,category,price,inventory,supplier,Has_an_offer,offer_price,valid_until):
        self.ID = ID
        self.name = name
        self.category = category
        self.price = price
        self.inventory = inventory
        self.supplier = supplier
        self.Has_an_offer = Has_an_offer
        self.offer_price = offer_price
        data = valid_until.split('/')
        if len(data) == 3:
            self.valid_until = date(int(data[2]), int(data[1]), int(data[0]))
        else:
            self.valid_until = ""

    def place_an_item_on_sale(self,offer_price,valid_until):
        self.Has_an_offer = 1
        self.offer_price = offer_price
        self.valid_until = valid_until

    def updateProduct(self,name,category,price,inventory,supplier,Has_an_offer,offer_price,valid_until):
        self.name = name
        self.category = category
        self.price = price
        self.inventory = inventory
        self.supplier = supplier
        self.Has_an_offer = Has_an_offer
        self.offer_price = offer_price
        self.valid_until = valid_until

    def executeOrder(self,NumOfItems):
        self.inventory -= NumOfItems

    def __str__(self):
        info = "Product ID: "+str(self.ID)+"\n"
        info += "Name: "+self.name+"\nCategory: "+str(self.category)+"\nPrice: "+str(self.price)+"\nInventory: "+str(self.inventory)+"\nSupplier: "+self.supplier
        if(self.Has_an_offer == 0):
            info += "\nThis product does not have an offer"
        else:
            info += "\nOffer price: "+str(self.offer_price)+"\n"
            info += "The product is valid until: "+str(self.valid_until)+""
        return info