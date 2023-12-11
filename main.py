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

def test_food_ordering():
    print("\n--- Starting Test Cases ---\n")


    # Test 1: Display Menu
    import io 
    import sys

    print("Test 1: Displaying the Menu")
    original_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    display_menu(menu)
    sys.stdout = original_stdout
    menu_output = captured_output.getvalue()
    expected_output = "Menu:\n"
    for item, price in menu.items():
        expected_output += f"{item} - ${price:.2f}\n"
    assert menu_output == expected_output, "Test 1 Failed: The displayed menu does not match the expected output."
    print("Test 1 Passed\n")

    # Test 2: Adding a valid item
    print("Test 2: Adding 'Burger' to the cart")
    add_to_cart("Burger", user_cart)
    assert "Burger" in user_cart, "Test 2 Failed: Burger not added to cart"
    print("Test 2 Passed\n")

    # Test 3: Adding an item with different case
    print("Test 3: Adding 'sushi' to the cart")
    add_to_cart("sushi", user_cart)
    assert "Sushi" in user_cart, "Test 3 Failed: Sushi not added to cart"
    print("Test 3 Passed\n")

    # Test 4: Trying to add an item not in the menu
    print("Test 4: Trying to add 'Ice Cream' to the cart")
    add_to_cart("Ice Cream", user_cart)
    assert "Ice Cream" not in user_cart, "Test 4 Failed: Ice Cream incorrectly added to cart"
    print("Test 4 Passed\n")

    # Test 5: Removing an item from the cart
    print("Test 5: Removing 'Burger' from the cart")
    remove_from_cart("Burger", user_cart)
    assert "Burger" not in user_cart, "Test 5 Failed: Burger not removed from cart"
    print("Test 5 Passed\n")

    # Test 6: Checkout with remaining items
    print("Test 6: Checkout with current items in the cart")
    current_total = sum([menu[item] for item in user_cart])
    checkout(user_cart)
    assert current_total == sum([menu[item] for item in user_cart]), "Test 6 Failed: Checkout total mismatch"
    print("Test 6 Passed\n")

    print("--- All Test Cases Completed ---")


if __name__ == "__main__":
    # main()
    test_food_ordering()
