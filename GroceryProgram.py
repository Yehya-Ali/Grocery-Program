groceries = {"apple":2, "banana":1, "milk":3, "bread":2}

fruit = ""

cart = []

price = 0

while fruit != "done":

    fruit = input("What do you want to buy?")

    if fruit == "done":
        break
    
    quantity = int(input("How many do you want?"))

    for i in range(quantity):

        print(i)

        if fruit in groceries:
            cart.append(fruit)
            i-=1
        
        else:
            print("Sorry, we don't have that item.")

for i in cart:
    if i in groceries:
        price += groceries[i]

print(f"You bought: {cart}")
print(f"Total: ${price}")

if price == 0:
    print("Your cart is empty!")

elif price > 10:
    print("You spent a lot!")

else:
    print("You spend a little!")