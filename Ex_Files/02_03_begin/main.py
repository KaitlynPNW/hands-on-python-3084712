NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0] #can access like an array in other languages
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] #names to the left of 2 (last two items of the list)
GEORGE_RINGO = NAMES[2:] #get 2 names to the right of : (first two items of the list)
REVERSE = NAMES[::-1] #start:stop:step
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)
