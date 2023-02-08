NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

print("traditional while loop")

i = 0 #traditional while loop
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

print("\n for in loop")

# more popular loop
for name in NAMES: #for each name in names
    print(name)

for name, age in zip(NAMES, AGES): #iterate through two collections at once, this does not create a new list in memory
    print(f"{name} {age}")

for name in reversed(NAMES): #won't take up space in memory
    print(name)

for i in range(5):
    print(i)

# enumerate -- so you know what index you are on in the for in loops
print("\n enumerate")
for i, name in enumerate(NAMES):
    print(f"{i} {name}")

