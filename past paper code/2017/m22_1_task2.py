num_students = 30

ages = [11, 10, 12, 6, 6, 10, 11, 6, 8, 12, 7, 7, 10, 10, 7, 11, 7, 8, 6, 11, 12, 6, 10, 6, 8, 11, 11, 11, 9, 10]
houses = ['Mars', 'Mars', 'Mars', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Saturn', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Saturn', 'Saturn', 'Mars', 'Mars', 'Saturn', 'Saturn', 'Saturn', 'Saturn', 'Saturn']
reaction_times = [61.5, 66.4, 74.2, 65.2, 65.5, 24.3, 42.3, 30.3, 61.1, 77.8, 48.7, 79.9, 64.8, 35.6, 75.3, 22.7, 97.2, 28.7, 59.5, 43.0, 0.4, 19.8, 28.4, 2.5, 61.5, 73.7, 17.9, 24.5, 52.0, 38.9]

reactionTimeSaturn = 0
reactionTimeMars = 0
countSaturn = 0
countMars = 0

for i in range(num_students):
    if houses[i] == "Saturn":
        reactionTimeSaturn += reaction_times[i]
        countSaturn += 1

    elif houses[i] == "Mars":
        reactionTimeMars += reaction_times[i]
        countMars += 1

print("Average reaction times for students in Saturn:", reactionTimeSaturn / countSaturn)
print("Average reaction times for students in Mars:", reactionTimeMars / countMars)

