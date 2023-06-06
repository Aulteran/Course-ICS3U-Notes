# SHOPPING CART ASSIGNMENT
# You have been tasked with creating the back end of a new app to store and edit grocery lists, called
# Grocify. The company has asked that you call your list shopping_cart and that you have the following
# menu items on the app. The Menu should look as follows.

menu = '''
1) Add item to shopping_cart
2) See shopping cart list
3) Remove item from shopping cart (according to index)
4) Edit item in shopping cart list (according to index)
5) Remove all items from the shopping cart
6) Exit

Make Selection Here: '''

# ICS 3U – ADD-ON
# Each of these options should be in their own separate function (besides exit) and should pass the list
# shopping_cart through as a parameter each time.

print("Welcome to Grocify")

shopping_cart = []

def add_item(cart: list):
    item = input("Enter item to add to shopping cart: ")
    cart.append(item)
    print(item, "added to shopping cart.")

def show_cart(cart: list):
    print("Shopping cart:")
    for item in cart:
        print(item)

def remove_item(cart: list):
    item_index = int(input("Enter index of item to remove from shopping cart: "))
    item = cart[item_index]
    del cart[item_index]
    print(item, "removed from shopping cart.")

def edit_item(cart: list):
    item_index = int(input("Enter index of item to edit in shopping cart: "))
    item = cart[item_index]
    new_item = input("Enter new item: ")
    cart[item_index] = new_item
    print(item, "in shopping cart edited to", new_item)

def clear_cart(cart: list):
    cart.clear()
    print("Shopping cart cleared.")

while True:
    menu_select = int(input(menu))
    if menu_select == 1:
        add_item(shopping_cart)
    elif menu_select == 2:
        show_cart(shopping_cart)
    elif menu_select == 3:
        remove_item(shopping_cart)
    elif menu_select == 4:
        edit_item(shopping_cart)
    elif menu_select == 5:
        clear_cart(shopping_cart)
    elif menu_select == 6:
        break
    else:
        print("Invalid selection.")

print("Thank You for choosing Grocify")