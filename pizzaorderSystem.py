pricePerUnitArea = 0.55
pricePerTopping = 1.25
pi = 3.1414
taxRateHigh = 0.085
taxRateLow = 0.05
radiusFactor = 1.15

# Prompt user for pizza size
pizzaSize = int(input("Enter pizza size: "))

# Validate pizza size
if pizzaSize not in [1, 2, 3]:
    pizzaSize = 1

# Calculate pizza radius
pizzaRadius = pizzaSize * radiusFactor

# Calculate pizza area
pizzaArea = pi * (pizzaRadius ** 2)

# Prompt for number of toppings
numToppings = int(input("Enter the number of toppings: "))

# Validate toppings count
if numToppings < 0 or numToppings > 8:
    numToppings = 1

# Prompt for quantity
quantity = int(input("Enter quantity: "))

# Validate quantity
if quantity < 0:
    quantity = 1
elif quantity > 50:
    quantity = 50

# Calculate pizza area price
pizzaAreaPrice = pizzaArea * pricePerUnitArea * quantity

# Calculate toppings price
toppingsPrice = pricePerTopping * numToppings * quantity

# Calculate sale price
salePrice = pizzaAreaPrice + toppingsPrice

# Calculate tax
if salePrice > 100:
    tax = salePrice * taxRateHigh
else:
    tax = salePrice * taxRateLow

# Calculate total price
totalPrice = salePrice + tax

# Display results
print(f"Pizza area price: ${pizzaAreaPrice:.2f}")
print(f"Toppings price: ${toppingsPrice:.2f}")
print(f"Sale price: ${salePrice:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total price: ${totalPrice:.2f}")
