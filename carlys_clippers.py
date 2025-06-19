"""
Carly's Clippers

You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have 
been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of 
the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.
Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in 
the last_week list. Each of these elements are in the first index of their respective lists.
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
### Create a variable to be added the prices to it
total_price = 0 

for price in prices:
  total_price += price
# print(total_price)

### Calculate the average price of haircuts
average_price = total_price / len(prices)
print(f"- Average Haircut Price: ${average_price}")

### Cutting all the prices by $5
new_prices = [price - 5 for price in prices]
print(f"- New Prices List: ${new_prices}")

### Calculating the total revenue from last week's sales
total_revenue = 0 

for i in range(0, len(hairstyles)):
  total_revenue += prices[i]
  total_revenue += last_week[i]  
  total_revenue += prices[i] * last_week[i]

print(f"- Total Revenue: ${total_revenue}")

### Finding the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"- Average Daily Revenue: ${average_daily_revenue:.2f}")

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(f"- Cuts Under $30: {cuts_under_30}")







