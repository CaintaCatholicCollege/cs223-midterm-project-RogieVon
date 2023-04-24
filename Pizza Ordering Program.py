# Rogie Von C. Ibañez
# BSCS 2-A
print("Welcome to the Pizza Ordering System!")
print("-------------------------------------")

# Display menu of pizza sizes and their corresponding prices
print("Pizza Sizes:")
print("1. Small ($5.00)")
print("2. Medium ($7.00)")
print("3. Large ($9.00)")

# Ask the user to choose a pizza size
size_choice = input("Choose a pizza size (1-3): ")

# Determine the size and price of the pizza based on the user's choice
if size_choice == "1":
    size = "Small"
    price = 5.00
elif size_choice == "2":
    size = "Medium"
    price = 7.00
elif size_choice == "3":
    size = "Large"
    price = 9.00
else:
    print("Invalid choice. Please choose a number between 1 and 3.")
    exit()

# Display menu of toppings and their corresponding prices
print("\nToppings:")
print("1. Cheese ($1.00)")
print("2. Pepperoni ($2.50)")
print("3. Mushrooms ($3.25)")
print("4. Olives ($0.50)")

# Ask the user to choose the number of toppings they want
num_toppings_choice = input("Choose the number of toppings (1-4): ")

# Calculate the total cost of the pizza based on the number of toppings
if num_toppings_choice == "1":
    num_toppings = 1
    topping_cost = 1.00
elif num_toppings_choice == "2":
    num_toppings = 2
    topping_cost = 2.50
elif num_toppings_choice == "3":
    num_toppings = 3
    topping_cost = 3.25
elif num_toppings_choice == "4":
    num_toppings = 4
    topping_cost = 0.50
else:
    print("Invalid choice. Please choose a number between 1 and 4.")
    exit()

# Calculate the total cost of the pizza
total_cost = price + topping_cost

# Display the details of the pizza order and the total cost
print("\nYour Pizza Order:")
print("Size: " + size)
print("Toppings: " + str(num_toppings))
print("Total Cost: $" + str(total_cost))