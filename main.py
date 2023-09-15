from datetime import date
import Product
import User

#reading files here
products = []
users = []

#reading files
#reading and storing the users in the system
f = open("user.txt","r")
lineNum = 0
for i in f:
    lineNum += 1
    basket = {} #empty to put values in it
    data = i.split(';')
    if len(data) == 5:
        try:
            user = User.User(int(data[0]),str(data[1]),str(data[2]),str(data[3]),int(data[4]),{},0)
            users.append(user)
        except ValueError:
            print("Invalid admin information on line #" + str(lineNum) + " in 'users.txt' file")
    elif len(data) == 7:
        temp = data[5].strip('{}').split(',')
        for j in temp:
            temp1 = j.split(':')
            key = temp1[0]
            value = temp1[1]
            basket[key] = value
        try:
            user = User.User(int(data[0]),str(data[1]),str(data[2]),str(data[3]),int(data[4]),basket,int(data[6]))
            users.append(user)

        except ValueError:
            print("Invalid shopper information on line #"+str(lineNum)+" in 'users.txt' file")
    else:
        print("Invalid user information on line #" + str(lineNum) + " in 'users.txt' file")

#reading and storing the products in the system
f = open("products.txt","r")
lineNum = 0
for i in f:
    lineNum += 1
    data = i.split(';')
    category_str = str(data[2].strip())
    category_str.lower()
    # Check if the category is in the mapping, if not, create a new enum member
    if category_str not in Product.Categories.__members__:
        Product.Categories.category_str = category_str
    category = Product.Categories.category_str
    if len(data) == 9:
        try:
            product = Product.Product(int(data[0]),str(data[1]),category,int(data[3]),int(data[4]),str(data[5]),int(data[6]),int(data[7]),str(data[8]))
            products.append(product)
        except ValueError:
            print('Invalid user information on line #"+str(lineNum)+" in products.txt file"')
    elif len(data) == 7:
        try:
            product = Product.Product(int(data[0]), str(data[1]), category, int(data[3]), int(data[4]), str(data[5]),int(data[6]),0,"")
            products.append(product)
        except ValueError:
            print('Invalid user information on line #"+str(lineNum)+" in products.txt file"')

#checking if a specific product is exist in the system using the product ID
def isProductExist(product_id):
    for i in products:
        if i.ID == product_id:
            return 1
    return 0

#checking if a specific user is exist in the system using the user ID
def isUserExist(user_id):
    for i in users:
        if i.ID == user_id:
            return 1
    return 0

#add a product to the system
def addProduct():
    ID = input("Input the product ID: ")
    while 1:
        try:
            ID = int(ID)
            break
        except ValueError:
            print("Invalid input...")
            ID = input("Input the product ID: ")
    while len(str(ID)) != 6:
        print("product ID must be 6 digits only...")
        ID = input("Input the product ID: ")
        while 1:
            try:
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
                ID = input("Input the product ID: ")
    while isProductExist(ID):
        print("This ID is already exist")
        ID = input("Input the product ID: ")
        while 1:
            try:
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
                ID = input("Input the product ID: ")
        while len(str(ID)) != 6:
            print("product ID must be 6 digits only...")
            ID = input("Input the product ID: ")
            while 1:
                try:
                    ID = int(ID)
                    break
                except ValueError:
                    print("Invalid input...")
                    ID = input("Input the product ID: ")
    name = input("Input the product name: ")
    category_str = input("Input the category of the product: ")
    category_str.lower()
    if category_str not in Product.Categories.__members__:
        Product.Categories.category_str = category_str
    category = Product.Categories.category_str
    price = input("Input the price of the product: ")
    while 1:
        try:
            price = int(price)
            break
        except ValueError:
            print("Invalid input...")
            price = input("Input the price of the product: ")
    inventory = input("Input the inventory of the product: ")
    while 1:
        try:
            inventory= int(inventory)
            break
        except ValueError:
            print("Invalid input...")
            inventory = input("Input the inventory of the product: ")
    supplier = input("Input the supplier of the product: ")
    while 1:
        try:
            has_an_offer = input("Does this product have an offer? (input 1 if yes, 0 if no): ")
            has_an_offer = int(has_an_offer)
            if  has_an_offer == 1:
                offer_price = input("Input the offer price of the product: ")
                while 1:
                    try:
                        offer_price = int (offer_price)
                        break
                    except ValueError:
                        print("Invalid input...")
                        offer_price = input("Input the offer price of the product: ")
                valid_until = input("Input the valid until date for the product (d/m/y): ")
                temp = valid_until.split('/')
                while len(temp) != 3:
                    print("Invalid input...")
                    valid_until = input("Input the valid until date for the product (d/m/y): ")
                    temp = valid_until.split('/')
                product = Product.Product(ID,name,category,price,inventory,supplier,has_an_offer,offer_price,valid_until)
                products.append(product)
                print("The product has been added successfully....")
                break
            elif has_an_offer == 0:
                product = Product.Product(ID, name, category, price, inventory, supplier, has_an_offer,0,"")
                products.append(product)
                print("The product has been added successfully....")
                break
            else:
                print("Invalid input...")
        except ValueError:
            print("Invalid input...")

def placeItemOnSale():
    ID = input("Input the ID of the product: ")
    while 1:
        try:
            ID = int(ID)
            break
        except ValueError:
            print("Invalid input...")
            ID = input("Input the ID of the product: ")
    while not isProductExist(ID):
        print("No product with this ID...")
        ID = input("Input the ID of the product: ")
        while 1:
            try:
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
                ID = input("Input the ID of the product: ")
    for i in products:
        if i.ID == ID:
            if i.Has_an_offer == 1:
                print("This product is already on sale")
                print("the offer price is: "+str(i.offer_price))
                print("Thr valid until date is: "+str(i.valid_until))
            else:
                offer_price = input("Input the offer price of this product: ")
                while 1:
                    try:
                        offer_price = int (offer_price)
                        break
                    except ValueError:
                        print("Invalid input...")
                        offer_price = input("Input the offer price of this product: ")
                valid_until = input("Input the valid until date of this product: ")
                temp = valid_until.split('/')
                while len(temp) != 3:
                    print("Invalid input...")
                    valid_until = input("Input the valid until date for the product (d/m/y): ")
                    temp = valid_until.split('/')
                i.place_an_item_on_sale(offer_price,valid_until)
                print("The product has been placed on sale successfully...")

def updateProduct():
    ID = input("Input the ID of the product: ")
    while 1:
        try:
            ID = int(ID)
            break
        except ValueError:
            print("Invalid input...")
            ID = input("Input the ID of the product: ")
    while not isProductExist(ID):
        print("No product with this ID...")
        ID = input("Input the ID of the product: ")
        while 1:
            try:
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
                ID = input("Input the ID of the product: ")
    for i in products:
        if  i.ID == ID:
            while 1:
                print("\n\nPlease Choose What you want to Update For The Product: ")
                print("1. Product Name ")
                print("2. Product Category ")
                print("3. Product Price")
                print("4. Product Inventory")
                print("5. Product Supplier ")
                print("6. Product Has an Offer  ")
                choice = input("Your choice: ")
                try:
                    choice = int (choice)
                except ValueError:
                    print("Invalid input...")
                    continue
                if choice >= 1 and choice <= 6:
                    break
                else:
                    print("choose a number between 1 and 6...")
            if choice == 1:
                name = input("Input the new name of the product: ")
                i.name = name
                print("\nThe product has been updated successfully....")
            elif choice == 2:
                category_str = input("Input the category of the product: ")
                category_str.lower()
                if (category_str not in Product.Categories.__members__):
                    Product.Categories.category_str = category_str
                category = Product.Categories.category_str
                i.category = category
                print("\nThe product has been updated successfully....")
            elif choice == 3:
                while 1:
                    try:
                        price = input("Input the price of the product: ")
                        price = int(price)
                        i.price = price
                        print("\nThe product has been updated successfully....")
                        break
                    except ValueError:
                        print("Invalid input...")
            elif choice == 4:
                while 1:
                    try:
                        inventory = input("Input the inventory of the product: ")
                        inventory = int(inventory)
                        i.inventory = inventory
                        print("\nThe product has been updated successfully....")
                        break
                    except ValueError:
                        print("Invalid input...")
            elif choice == 5:
                supplier = input("Input the suppplier of the product: ")
                supplier.lower()
                i.supplier = supplier
                print("\nThe product has been updated successfully....")
            elif choice == 6:
                while 1:
                    try:
                        has_an_offer = input("Does this product have an offer? (input 1 if yes, 0 if no): ")
                        has_an_offer = int(has_an_offer)
                        if has_an_offer == 1 or has_an_offer == 0:
                            i.Has_an_offer = has_an_offer
                        else:
                            print("Invalid input...")
                            continue
                        if i.Has_an_offer == 1:
                            while 1:
                                try:
                                    offer_price = input("Input the offer price of this product: ")
                                    offer_price = int(offer_price)
                                    i.offer_price = offer_price
                                    break
                                except ValueError:
                                    print("Invalid input...")
                            while 1:
                                try:
                                    valid_until = input("Input the valid until date of this product (d/m/y): ")
                                    data = valid_until.split('/')
                                    while len(data) != 3:
                                        print("Invalid input, enter the date as this form (d/m/y)")
                                        valid_until = input("Input the valid until date of this product (d/m/y): ")
                                        data = valid_until.split('/')
                                    i.valid_until = date(int(data[2]), int(data[1]), int(data[0]))
                                    print("\nThe product has been updated successfully....")
                                    break
                                except ValueError:
                                    print("Invalid input...")
                            break
                        else:
                            print("\nThe product has been updated successfully....")
                            break
                    except ValueError:
                        print("Invalid input...")

def addUser():
    while 1:
        ID = input("Input the user ID: ")
        try:
            ID = int(ID)
            break
        except ValueError:
            print("Invalid input...")
    while len(str(ID)) != 6:
        print("user ID must be 6 digits only...")
        while 1:
            ID = input("Input the user ID: ")
            try:
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
    while isUserExist(ID):
        print("This ID is already exist")
        while 1:
            ID = input("Input the user ID: ")
            try:
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
        while len(str(ID)) != 6:
            print("user ID must be 6 digits only...")
            while 1:
                ID = input("Input the user ID: ")
                try:
                    ID = int(ID)
                    break
                except ValueError:
                    print("Invalid input...")
    name = input("Input the user name: ")
    DoB = input("Input the user's date of birth: ")
    temp = DoB.split('/')
    while len(temp) != 3:
        print("Invalid input...")
        DoB = input("Input the user's date of birth: ")
        temp = DoB.split('/')
    role = input("Input the role of the user (shopper/admin): ")
    role = role.lower()
    while role != "shopper" and role != "admin":
        print("Invalid input")
        role = input("Input the role of the user (shopper/admin): ")
    active = input("Is the user active (1) or not (0): ")
    while 1:
        try:
            active = int (active)
            if active == 0 or active == 1:
                break
            else:
                print("Invalid input...")
                active = input("Is the user active (1) or not (0): ")
        except ValueError:
            print('Invalid input...')
            active = input("Is the user active (1) or not (0): ")
    user = User.User(ID,name,DoB,role,active,"",0)
    users.append(user)
    print("The user has been added successfully")

def updateUser():
    ID = input("Input the ID of the user: ")
    while 1:
        try:
            ID = int(ID)
            break
        except ValueError:
            print("Invalid input...")
            ID = input("Input the ID of the user: ")
    while not isUserExist(ID):
        print("No user with this ID,try again...")
        while 1:
            try:
                ID = input("Input the ID of the user: ")
                ID = int(ID)
                break
            except ValueError:
                print("Invalid input...")
    for i in users:
        if  i.ID == ID:
            while 1:
                print("Please Choose What you want to Update For The User: ")
                print("1. User Name ")
                print("2. User Date Of Birthday  ")
                print("3. User Role ")
                print("4. User Active")
                choice = input("Your choice: ")
                try:
                    choice = int (choice)
                except ValueError:
                    print("Invalid input...")
                    continue
                if choice >= 1 and choice <= 4:
                    break
                else:
                    print("choose number between 1 and 4")
            if choice == 1:
                name = input("Input the user name: ")
                i.name = name
                print("\nThe user has been updated successfully...\n")
            elif choice == 2:
                DoB = input("Input the user's date of birth (d/m/y): ")
                data = DoB.split('/')
                while len(data) != 3:
                    print("Invalid input, enter the date as this formate (d/m/y)")
                    DoB = input("Input the user's date of birth (d/m/y): ")
                    data = DoB.split('/')
                i.DoB = date(int(data[2]),int(data[1]),int(data[0]))
                print("\nThe user has been updated successfully...\n")
            elif choice == 3:
                role2 = input("Input the role of the user (shopper/admin): ")
                role2 = role2.lower()
                while (role2 != "shopper" and role2 != "admin"):
                    print("Invalid input")
                    role2 = input("Input the role of the user (shopper/admin): ")
                i.role = role2
                print("\nThe user has been updated successfully...\n")
            elif choice == 4:
                while 1:
                    try:
                        active = input("Is the user active (1) or not (0): ")
                        active = int(active)
                        if active == 0 or active == 1:
                            i.active = active
                            print("\nThe user has been updated successfully...\n")
                            break
                        else:
                            print("Invalid input...")
                    except ValueError:
                        print("Invalid input...")

def DissplayAllUsers():
    print("\nUsers in the system......\n\n")
    for i in users:
        print(str(i.__str__()))
        print("------------------------------")

def DisplayProducts():
    while 1:
        print("\nPlease Choose What you want to  List  From Products: ")
        print("1. List All Products  ")
        print("2. List Offers Products   ")
        print("3. List Category Products  ")
        print("4. List Name Products")
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 4:
                break
            else:
                print("choose between 1 and 4")
        except ValueError:
            print("Invalid input...")
    print("\n\n")
    if choice == 1:
        for i in products:
            print(i.__str__())
            print("\n")
        if len(products) == 0:
            print("No products added to the system yet...")
    elif choice == 2:
        for i in products:
            if i.Has_an_offer == 1:
                print(i.__str__())
                print("\n")
    elif choice == 3:
        category = input("Input the category: ")
        category.lower()
        for i in products:
            if i.category == category:
                print(i.__str__())
                print("\n")
    elif choice == 4:
        name = input("Input the name of the product: ")
        for i in products:
            if i.name == name:
                print(i.__str__())
                print("\n")

def addProductToTheBasket(user_id):
    product_id = input("Input the ID of the product to be added: ")
    while 1:
        try:
            product_id = int(product_id)
            break
        except ValueError:
            print("Invalid input...")
            product_id = input("Input the ID of the product to be added:")
    while not isProductExist(product_id):
        print("No product with this ID, try again")
        product_id = input("Input the ID of the product to be added: ")
        while 1:
            try:
                product_id = int(product_id)
                break
            except ValueError:
                print("Invalid input...")
                product_id = input("Input the ID of the product to be added:")
    #check if this ID is exist in the shopper's basket
    for i in users:
        if i.ID == user_id:
            for j in i.basket:
                if int(j) == product_id:
                    print("This product is already exist in your basket...\n")
                    return
    while 1:
        numOfItems = input("Input number of items from this product to be added: ")
        try:
            numOfItems = int(numOfItems)
            break
        except ValueError:
            print("Invalid input...")
    for i in users:
        if i.ID == user_id:
            i.addItemToBasket(product_id,numOfItems)
            print("The product had been added to the basket successfully...")
            break

def displayBasket(user_id):
    sum = 0
    for i in users:
        if i.ID == user_id:
            if len(i.basket) == 0:
                print('Your basket is empty...')
                return
            for j in i.basket:
                print("\n\nProduct ID: "+str(j))
                for k in products:
                    if k.ID == int(j):
                        print("Product name: "+str(k.name))
                        print("Product category: "+str(k.category))
                        print("Price: "+str(k.price))
                        print("Supplier: "+str(k.supplier))
                        print("Has an offer: "+str(k.Has_an_offer))
                        if k.Has_an_offer == 1:
                            print("offer price: "+str(k.offer_price))
                            print("valid until: "+str(k.valid_until))
                            print("Number of Items: " + str(i.basket[j]))
                            cost = int(int(i.basket[j]) * k.offer_price)
                            print("Cost of purchase of the product: " + str(cost))
                            sum += cost
                        else:
                            print("Number of Items: "+str(i.basket[j]))
                            print("offer price:valid until = 0/0/0")
                            cost = int (int(i.basket[j]) * k.price)
                            print("Cost of purchase of the product: "+str(cost))
                            sum += cost
    print("\nBasket cost: "+str(sum))

def updateBasket(user_id):
    while 1:
        print("\nPlease choose one of the following options (1-3):")
        print("1- Clear the basket")
        print("2- Remove a specific product from the basket")
        print("3- Update the number of items for a specific product")
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 3:
                break
            else:
                print("Invalid input..")
        except ValueError:
            print("Invalid input..")
    for i in users:
        if i.ID == user_id:
            if choice == 1:
                i.clearBasket()
                print("\nThe basket has been cleared successfully...")
            elif choice == 2:
                product_id = input("Input the product ID to be removed from the basket: ")
                while 1:
                    try:
                        product_id = int (product_id)
                        break
                    except ValueError:
                        print("Invalid input...")
                        product_id = input("Input the product ID to be removed from the basket: ")
                found = 0
                for j in i.basket:
                    if int(j) == product_id:
                        found = 1
                        i.removeProduct(product_id)
                        print("Product has been removed from the basket successfully...")
                if found == 0:
                    print("This product does not exist in your basket...")
                    break
            elif choice == 3:
                product_id = input("Input the product ID to be updated from the basket: ")
                while 1:
                    try:
                        product_id = int(product_id)
                        break
                    except ValueError:
                        print("Invalid input...")
                        product_id = input("Input the product ID to be removed from the basket: ")
                found = 0
                for j in i.basket:
                    if  int(j) == product_id:
                        found = 1
                        numOfItems = input("Input the new number of items for this product: ")
                        numOfItems = int(numOfItems)
                        i.updateBasket(product_id, numOfItems)
                        print("The basket has been updated successfully...")
                if found == 0:
                    print("This product does not exist in your basket...")
                    break

def placeAnOrder(user_id):
    for i in users:
        if i.ID == user_id:
            i.placeAnOrder()

def executeOrder():
    for i in users:
        if i.order == 1:
            for j in i.basket:
                items = i.basket[j]
                items = (int) (items)
                for k in products:
                    if k.ID == int(j):
                        if (k.inventory - items) >= 0:
                            k.executeOrder(items)
                            print("\nUser: " + i.name + ", ID: " + str(i.ID) + " order has been executed successfully...")
                            i.clearBasket()
                            i.order = 0
                        else:
                            print("\norder of the shopper: "+str(i.name)+", ID: "+str(i.ID)+
                                  "\ncan't be executed since there is no enough inventory of the product ID: "+str(k.ID))

def saveProducts():
    filename = input("Input the file name to save the products information in: ")
    f = open(filename, "w")
    for i in products:
        f.write(str(i.ID)+";")
        f.write(str(i.name)+";")
        f.write(str(i.category)+";")
        f.write(str(i.price) + ";")
        f.write(str(i.inventory) + ";")
        f.write(str(i.supplier) + ";")
        f.write(str(i.Has_an_offer) + ";")
        if i.Has_an_offer == 1:
            f.write(str(i.Has_an_offer) + ";")
            f.write(str(i.offer_price) + ";")
            f.write(str(i.valid_until))
        else:
            f.write(str(i.Has_an_offer))
        f.write("\n")

def saveUsers():
    filename = input("Input the file name to save the users information in: ")
    f = open(filename, "w")
    for i in users:
        f.write(str(i.ID) + ";")
        f.write(str(i.name) + ";")
        f.write(str(i.DoB) + ";")
        f.write(str(i.role) + ";")
        f.write(str(i.active) + ";")
        f.write(str(i.basket) + ";")
        f.write(str(i.order))
        f.write("\n")

def listShoppers():
    while 1:
        print("\nChoose one of the following options (1-3): ")
        print("1- List all shoppers")
        print("2- List all shoppers who have added items for their basket")
        print("3- List all shoppers who have unprocessed order")
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if choice >= 1 and choice <= 3:
                break
            else:
                print("Invalid input...")
        except ValueError:
            print("Invalid input...")

    for i in users:
        if  choice == 1:
            if i.role == "shopper":
                print("User: "+i.name+", ID: "+str(i.ID))
        elif choice == 2:
            if(len(i.basket) != 0):
                print("User: "+i.name+", ID: "+str(i.ID))
        elif choice == 3:
            if i.order == 1:
                print("User: " + i.name + ", ID: " + str(i.ID))


#log in process here
print("Welcom to our E-commerce System\n")
print("Log in the system.....")
role = -1
ID = 0
while 1:
    found = 0
    ID = input("Your ID: ")
    try:
        ID = int(ID)
    except ValueError:
        print("Invalid input...")
        continue
    for i in users:
      if  i.ID == ID:
          found = 1
          if i.role == "shopper":
              role = 0
              print("Welcome our dear shopper")
              break
          elif i.role == "admin":
             role = 1
             print("Welcome our dear admin")
             break
    if  found == 0:
        print("This ID does not exist in the system, try again....\n")
    if  role != -1:
        break
dirty = 0
while 1:

    print("\n---------------------------------------------------\n")
    print("Please choose one of the following optiona:")
    print ("1.  Add product ")
    print ("2.  Place an item on sale ")
    print ("3.  Update product ")
    print ("4.  Add a new user")
    print ("5.  Update user")
    print ("6.  Display all users ")
    print ("7.  List products ")
    print ("8.  List shoppers ")
    print ("9.  Add product to the basket")
    print ("10. Display basket")
    print ("11. Update basket")
    print ("12. Place order ")
    print ("13. Execute order ")
    print ("14. Save products to a file ")
    print ("15. Save users to a text file ")
    print ("16. Exit")
    choice = input("Your choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input...")
        continue

    if choice == 1:
        if role == 1:
            dirty = 1
            addProduct()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 2:
        if role == 1:
            dirty = 1
            placeItemOnSale()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 3:
        if  role == 1:
            dirty = 1
            updateProduct()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 4:
        if  role == 1:
            dirty = 1
            addUser()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 5:
        if  role == 1:
            dirty = 1
            updateUser()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 6:
        if  role == 1:
            DissplayAllUsers()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 7:
        DisplayProducts()
    elif choice == 8:
        if  role == 1:
            listShoppers()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 9:
        if  role == 0:
            dirty = 1
            addProductToTheBasket(ID)
        else:
            print("As an admin, you don't have the permission to do this process")
    elif choice == 10:
        if  role == 0:
            displayBasket(ID)
        else:
            print("As an admin, you don't have the permission to do this process")
    elif choice == 11:
        if  role == 0:
            dirty = 1
            updateBasket(ID)
        else:
            print("As an admin, you don't have the permission to do this process")
    elif choice == 12:
        if  role == 0:
            dirty = 1
            placeAnOrder(ID)
        else:
            print("As an admin, you don't have the permission to do this process")
    elif choice == 13:
        if  role == 1:
            dirty = 1
            executeOrder()
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 14:
        if  role == 1:
            saveProducts()
            dirty = 0
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 15:
        if  role == 1:
            saveUsers()
            dirty = 0
        else:
            print("As a shopper, you don't have the permission to do this process")
    elif choice == 16:
        if dirty == 1:
            while 1:
                answer = input("Are you sure you want to exit without saving? (yes/no): ")
                answer.lower()
                if answer == "no":
                    break
                elif answer == "yes":
                    print("\nlogging out has been done successfully")
                    print("See you later...")
                    exit(1)
                else:
                    print("Invalid input...")
        else:
            print("\nlogging out has been done successfully")
            print("See you later...")
            exit(1)
    else:
        print("Invalid input...")
        print("------------------------------------------------------")
