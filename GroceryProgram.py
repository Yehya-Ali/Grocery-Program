groceries = {"apple":2, "banana":1, "milk":3, "bread":2}

item = ""

cart = {}

price = 0

while item != "done":

    item = input("What do you want to buy?")

    if item == "done":
        break

    if item in groceries:
    
        quantity = int(input("How many do you want?"))

        cart[item] = quantity

        price += (groceries[item] * cart[item])

        if item == "milk" and quantity > 2:

            price -=1

    else:

        print("Sorry, we don't have that item.")

print(f"You bought: {cart}")
print(f"Total: ${price}")

if price == 0:
    print("Your cart is empty!")

elif price > 10:
    print("You spent a lot!")

else:
    print("You spend a little!")