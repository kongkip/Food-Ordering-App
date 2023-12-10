menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Drink": 1.99,
    "Sushi": 9.99,
    "Pizza": 7.99,
}


def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item} - ${price:.2f}")


user_cart = []

def add_to_cart(item, cart):
    item = item.capitalize() # Capitalize first letter
    if item in menu:
        cart.append(item)
        print(f"{item} added to cart")
    else:
        print(f"{item} not in menu")


def remove_from_cart(item, cart):
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart")
    else:
        print(f"{item} not in cart")


def checkout(cart):
    total = sum([menu[item] for item in cart])
    print(f"Your total is ${total:.2f}")


def main():
    display_menu(menu)
    while True:
        print("Enter an item to add to cart, or type 'checkout' to checkout")
        item = input(">> ")
        if item == "checkout":
            checkout(user_cart)
            break
        else:
            add_to_cart(item, user_cart)


if __name__ == "__main__":
    main()
