fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes", 
  "Pineapple", "Papaya", "Guava", "Watermelon", "Strawberry"}
summer_fruits = {"Mango", "Watermelon", "Papaya", "Litchi", "Pineapple"}
winter_fruits = {"Apple", "Orange", "Strawberry", "Guava", "Grapes"}



print("Fruits:", fruits)
print("Summer Fruits:", summer_fruits)
print("Winter Fruits:", winter_fruits)


print("\nFruits and Winter Fruits:")
print(fruits & winter_fruits)

print("\nSummer fruits but not in Fruits:")
print(summer_fruits - fruits)


print("Summer ∩ Winter but not in fruits:", (summer_fruits & winter_fruits) - fruits)


print("\nIs Orange present in Fruits?")
print("Orange" in fruits)
