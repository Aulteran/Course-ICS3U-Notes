shopping_cart = []

def addItem(shoppingCart):
    item = input("What item would you like to add?:")
    shoppingCart.append(item)
    print(item, "is added to the cart now")

def viewCart(shoppingCart):
    print("your cart has the following", shoppingCart)

def removeItem(shoppingCart):
    print(shoppingCart)
    removeNum = int(input("What index would you like to remove?:"))
    shoppingCart.remove(shoppingCart[removeNum])
    print("item has been removed")

def editItem(shoppingCart):
    edit = int(input("At what index would you like to edit?:"))
    newedit = input("What would you like to change it too?")
    shoppingCart[edit]=newedit
    print(shoppingCart)
  

def removeAll(shoppingCart):
    shoppingCart.clear()
    print("All items removed")


def shoppingcart():
    print("Welcome to Grocify!")

    print("""
    Options
    1) Add item to shopping_cart
    2) See shopping cart list
    3) Remove item from shopping cart (according to index)
    4) Edit item in shopping cart list (according to index)
    5) Remove all items from the shopping cart
    6) Exit
    """)

    option = int(input("Which option would you like to choose?:"))
    try:
        if option==1:
            addItem(shopping_cart)
        if option==2:
            viewCart(shopping_cart)
        if option==3:
            removeItem(shopping_cart)
        if option==4:
            editItem(shopping_cart)
        if option==5:
            removeAll(shopping_cart)
        if option==6:
            return
        else:
            ("Number not in range, choose a number within the options")
            shoppingcart()
        print("Your shopping cart is", shopping_cart, "Thank you for shopping")
    except (ValueError):
        print("Invalid input, not an integer, try again")
        shoppingcart()
shoppingcart()