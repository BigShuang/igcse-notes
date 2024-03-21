# constant, integer, maximum number of votes that can be cast
maxVotes = 4
# number of candidates 
noCandidates = [
    1, 2, 1, 3, 3, 1, 2, 3, 3, 3, 
    1, 3, 4, 1, 1, 1, 1, 1, 4, 4,
    1, 4, 1, 2, 2, 1, 3, 3, 4, 2
]

totalNoCandidateVotes = [0, 0, 0, 0]

for i in range(30):
    num = noCandidates[i]
    totalNoCandidateVotes[num-1] = totalNoCandidateVotes[num-1] + 1

print(totalNoCandidateVotes)

maxVoteCount = 0
maxIndex = -1
for i in range(maxVotes):
    if totalNoCandidateVotes[i] > maxVoteCount:
        maxIndex = i + 1
        maxVoteCount = totalNoCandidateVotes[i] 

print(maxIndex, maxVoteCount)

maxCount = 0
for i in range(maxVotes):
    if totalNoCandidateVotes[i] == maxVoteCount:
        maxCount += 1

if maxCount > 1:
    print("NO OVERALL WINNER")
else:
    print("NEW CLASS CAPTAIN", maxIndex)
