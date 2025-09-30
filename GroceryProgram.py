groceries = {"apple":2, "banana":1, "milk":3, "bread":2}

item = ""

cart = {}

price = 0

while item != "done":

    item = input("What do you want to buy?")

    if item == "done":
        break

    elif item in groceries:
    
        quantity = int(input("How many do you want?"))

        cart[item] = quantity

        price += (groceries[item] * cart[item])

    else:
        print("Sorry, we don't have that item.")

if "milk" in cart and cart["milk"] > 2:

    price -=1

if price == 0:
    print("Your cart is empty!")

elif price > 10:
    print("You spent a lot!")
    print(f"You bought: {cart}")
    print(f"Total: ${price}")

else:
    print("You spend a little!")
    print(f"You bought: {cart}")
    print(f"Total: ${price}")