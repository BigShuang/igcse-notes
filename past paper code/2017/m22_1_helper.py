import random


num_students = 50

ages = []
houses = []
reaction_times = []

for i in range(num_students):
    age = random.randint(6, 12)
    house = random.choice(["Saturn", "Mars"])
    rt = round(random.random() * 100, 1)
    ages.append(age)
    houses.append(house)
    reaction_times.append(rt)

print(ages)
print(houses)
print(reaction_times)