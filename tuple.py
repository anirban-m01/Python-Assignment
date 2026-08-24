employees = (
    "Anirban", "Mehu", "Soumitra", "Anirban", "Sonai", "Pinaki", "Akash", "Buddha",
    "Mehu", "Rima", "Riya", "Suman", "Soumitra", "Akash", "Sonai", "Milon",
    "Neha", "Rima", "Suman", "Mehu"
)
# a. Print each name and frequency
print("Employee Frequency:")
for name in set(employees):
    print(name, ":", employees.count(name))

    # b. Remove duplicates and count distinct names
distinct_names = tuple(set(employees))
print("\nDistinct names tuple:", distinct_names)
print("Number of distinct names:", len(distinct_names))

# c. Employee with maximum frequency
max_name = max(set(employees), key=employees.count)
print("\nEmployee with maximum frequency:", max_name)

# d. Sort tuple alphabetically
sorted_names = tuple(sorted(employees))
print("\nSorted tuple:", sorted_names)

# e. Search for a specific employee name
search = input("\nEnter employee name to search: ")

if search in employees:
    print(search, "exists in the tuple.")
else:
    print(search, "does not exist.")