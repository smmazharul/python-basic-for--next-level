foods =[]
prices=[]
total = 0

while True:
    food = input("Enter the food item you want (q to quit): ")
    if food.lower()=='q':
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("------ Shopping Cart ------")
sum_price = sum(prices)
for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")
print("---------------------------")
print(f"Total: ${sum_price:.2f}")