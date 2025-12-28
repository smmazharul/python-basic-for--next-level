

# groceries = [["apples","bananas","avocados"],
#              ["carrots","broccoli","spinach"],
#              ["milk","eggs","cheese"]]
groceries = (("apples","bananas","avocados"),
             ("carrots","broccoli","spinach"),
             ("milk","eggs","cheese"))

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()