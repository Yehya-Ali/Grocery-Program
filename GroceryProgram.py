groceries = {"apple":2, "banana":1, "milk":3, "bread":2}

fruit = ""

cart = []

price = 0

while fruit != "done":

    fruit = input("What do you want to buy?")

    if fruit in groceries:
        cart.append(fruit)
        
    else:
        print("Sorry, we don't have that item.")

for i in cart:
    if i in groceries:
        price += groceries[i]

print(f"You bought: {cart}")
print(f"Total: ${price}")

if price > 10:
    print("You spent a lot!")

else:
    print("You spent a little!")