groceries = ["milk", "bread", "eggs", "butter", "cheese"]

# print(groceries[-1])
# print(dir(groceries))
# print (groceries.index("eggs"))
# print (groceries.count("bread"))
# groceries.append("yogurt")
# groceries.insert(2, "banana")
# groceries.remove("butter")
# groceries.pop(2)
# groceries.sort()
# groceries.reverse()

# for item in groceries:
#     print(item)

# groceries = {"milk", "bread", "eggs", "butter", "cheese"}

# print(groceries)
# print(dir(groceries))
# groceries.remove("milk")
# groceries.add("yogurt")
# groceries.update(["chocolate", "cookies"])
# groceries.discard("bread")
# groceries.pop()
# groceries.clear()

# for item in groceries:
#     print(item)

# groceries = ("milk", "bread","bread", "eggs", "butter", "cheese")

# print(groceries)
# # print(dir(groceries))
# print(groceries.count("bread"))
# groceries.index("eggs")
# groceries.pop()

# groceries = {
#     "dairy": ["milk", "cheese", "butter"],
#     "bakery": ["bread", "bagel", "muffin"],
#     "produce": ["apple", "banana", "carrot"],
#     "meat": ["chicken", "beef", "pork"]
# }

# groceries["beverages"] = ["coffee", "tea", "juice"]
# groceries.index("dairy")
# print(dir(groceries))
# print(groceries.keys())
# print(groceries.values())
# print(groceries.items())

# for value in groceries.values():
#     for item in value:
#         print(item,end=" ")
#     print()

# for key, value in groceries.items():
#     for item in value:
#         print(f"{item}")


menus = {
    "milk": 2.5,
    "bread": 1.5,
    "eggs": 3.0,
    "butter": 4.0,
    "cheese": 5.0
}
order_menu = []
total = 0
print("-------- Menu -------")
for key, value in menus.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------")

while True:
    item = input("Enter an item to add your order (q to quit): ").lower()
    if item == 'q':
        break
    elif menus.get(item) is not None:
        order_menu.append(item)

print("\n----- Your Order -----")
for order in order_menu:
    print(f"{order:13}: ${menus[order]:.2f}")
    
    total += menus[order]

print("---------------------")
print(f"Your total is: ${total:.2f}")
