num_students = 2
ages = [0 for i in range(num_students)]
houses = ['' for i in range(num_students)]
reaction_times = ['' for i in range(num_students)]

for i in range(num_students):
    print(f"Student {i + 1}:")
    age = input("Enter age (12-16): ")
    while not (12 <= int(age) <= 16):
        print("Invalid age! Please enter a valid age between 12 and 16.")
        age = input("Enter age (12-16): ")
    ages[i] = int(age)

    house = input("Enter school house (Saturn or Mars): ")
    while house!= "Saturn" and house!= "Mars":
        print("Invalid house! Please enter either 'Saturn' or 'Mars'.")
        house = input("Enter school house (Saturn or Mars): ")
    houses[i] = house

    reaction_time = input("Enter reaction time: ")
    while float(reaction_time) < 0:
        print("Invalid reaction time! Please enter a valid non-negative number.")
        reaction_time = input("Enter reaction time: ")
    reaction_times[i] = float(reaction_time)