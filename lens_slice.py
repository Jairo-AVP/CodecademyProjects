# Your code below:

# Make some pizzas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of occurrences of 2 in the price list 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
print("")

# Finding out the length of the topping list 
num_pizzas = len(toppings)
print(num_pizzas)
print("")

print(f"We sell {num_pizzas} different kinds of pizzas!")
print("")

# Creating a 2D list with toppings and prices 
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
print("")

# Sorting and Slicing Pizzas 
pizza_and_prices.sort()
print(pizza_and_prices)
print("")

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
print("")

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
print("")

# Removing the priciest pizza from the list
pizza_and_prices.pop()
print(pizza_and_prices)
print("")

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
print("")

# Looking for the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
print("")