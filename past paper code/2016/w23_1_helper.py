import random 

votes = []
for i in range(30):
    vote = random.choice(range(1,5))
    votes.append(vote)

print(votes)