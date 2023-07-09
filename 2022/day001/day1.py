# Read the input file and split it by blank lines
with open("adventofcode.com_2022_day_1_input.txt") as f:
    data = f.read().split("\n\n")
#print(data)
# Initialize a list to store the total calories of each elf
calories = []

# Loop through each elf's inventory
for elf in data:
#    # Split the inventory by newlines and convert each item to an integer
    items = [int(item) for item in elf.split("\n") if item != '']
#    # Sum up the calories of all the items and append it to the list
    calories.append(sum(items))

# Find the maximum value in the list and print it
max_calories = max(calories)
print(f"The elf carrying the most calories is carrying {max_calories} calories.")


calories.sort(reverse = True)


print(sum(calories[:3]))
