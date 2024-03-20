
num_students = 50
ages = [9, 11, 8, 7, 11, 6, 10, 10, 10, 6, 6, 7, 7, 7, 12, 11, 6, 10, 6, 7, 7, 10, 7, 12, 12, 8, 11, 8, 8, 11, 8, 9, 7, 12, 10, 10, 12, 8, 7, 6, 9, 8, 10, 7, 8, 8, 8, 12, 11, 11]
houses = ['Saturn', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Mars', 'Mars', 'Mars', 'Mars', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Saturn', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Mars', 'Mars', 'Mars', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Mars', 'Mars', 'Saturn', 'Saturn', 'Saturn']
reaction_times = [96.0, 51.4, 53.8, 12.0, 16.9, 96.7, 63.7, 62.6, 51.0, 35.4, 82.0, 15.6, 77.7, 58.5, 24.6, 94.9, 73.6, 59.8, 75.9, 95.3, 47.2, 56.1, 71.7, 40.3, 15.3, 31.2, 70.7, 58.3, 64.0, 45.3, 84.0, 64.7, 41.6, 17.0, 2.1, 1.8, 46.7, 30.5, 60.9, 66.0, 41.7, 59.9, 45.4, 87.5, 75.8, 97.7, 36.8, 0.8, 84.7, 20.8]

totalReactionTime = 0
count = 0
slowestReactionTime = -1

age = int(input("Enter age (12-16): "))
while not (12 <= age <= 16):
    print("Invalid age! Please enter a valid age between 12 and 16.")
    age = int(input("Enter age (12-16): "))


house = input("Enter school house (Saturn or Mars): ")
while house!= "Saturn" and house!= "Mars":
    print("Invalid house! Please enter either 'Saturn' or 'Mars'.")
    house = input("Enter school house (Saturn or Mars): ")

for i in range(num_students):
    if ages[i] == age and houses[i] == house:
        totalReactionTime += reaction_times[i]
        count += 1
        if slowestReactionTime == -1 or reaction_times[i] < slowestReactionTime:
            slowestReactionTime = reaction_times[i]

if count > 0:
    print("Average reaction time:", totalReactionTime / count)
    print("slowest reaction time:", slowestReactionTime)
else:
    print("No data")


