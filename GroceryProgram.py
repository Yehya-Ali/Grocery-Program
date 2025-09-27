groceries = {"apple":2, "banana":1, "milk":3, "bread":2}

fruit = ""

cart = {}

price = 0

while fruit != "done":

    fruit = input("What do you want to buy?")

    if fruit == "done":
        break
    
    quantity = int(input("How many do you want?"))

    if fruit in groceries:

        price += groceries[fruit] * quantity
        
        cart[fruit] = quantity

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