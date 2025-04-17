"""
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
"""


# weight = 8.4
weight = 1.5

# Ground Shipping 

if weight <= 2:
  cost_ground_shipping = (weight * 1.5) + 20.00
elif weight <= 6:
  cost_ground_shipping = (weight * 3.00) + 20.00
elif weight <= 10:
  cost_ground_shipping = (weight * 4.00) + 20.00
else :
  cost_ground_shipping = (weight * 4.75) + 20.00

print("The cost of ground shipping is: $" + str(cost_ground_shipping))
print("")

# Ground Shipping Premium 

cost_premium_ground_shipping = 125.00
print("The cost of premium ground shipping is: $" + str(cost_premium_ground_shipping))
print("")


# Drone Shipping 

if weight <= 2:
  cost_drone_shipping = (weight * 4.50)
elif weight <= 6:
  cost_drone_shipping = (weight * 9.00)
elif weight <= 10:
  cost_drone_shipping = (weight * 12.00)
else:
  cost_drone_shipping = (weight * 14.25)

print("The cost of drone shipping is: $" + str(cost_drone_shipping))

