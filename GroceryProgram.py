groceries = {"apple":2, "banana":1, "milk":3, "bread":2}

fruit = ""

cart = []

while fruit != "done":

    fruit = input("What do you want to buy?")

    if fruit in groceries:

        cart.append(fruit)
        
    else:

        print("Sorry, we don't have that item.")

print(f"You bought: {cart}")