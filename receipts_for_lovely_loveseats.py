"""
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet
Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts 
for your customers. In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process t
he total price and item list of customers, printing them to the output terminal

Spanish Translation:Hemos decidido perseguir el sueño de tener un pequeño negocio y abrir una mueblería llamada Lovely Loveseats para Neat Suites en Fleet Street. 
Con nuestros nuevos conocimientos de programación en Python, vamos a crear un sistema para agilizar el proceso de creación de recibos para sus clientes. 
En este proyecto, almacenaremos los nombres y precios del catálogo de una mueblería en variables. Luego, procesará el precio total y la lista de artículos de los clientes, 
imprimiéndolos en la terminal de salida.
"""

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade"
luxurious_lamp_price = 52.15

sales_tax = .088  # That is 8.8%

customer_one_total = 0
customer_one_itemization = ""

# Add the price of the Lovely Loveseat to the customer's total
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n" + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("")

print("Customer One Total:")
print(f"${customer_one_total}")