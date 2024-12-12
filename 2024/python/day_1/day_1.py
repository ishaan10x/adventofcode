import bisect

# PART 1
leftList = []
rightList = []
distanceList = []

# read ids into left and right list
with open('C:\\Users\\Ishaan\\myprojects\\adventofcode\\2024\\python\\day1\\input.txt', 'r') as file:
    for line in file:
        words = line.split()
        bisect.insort(rightList, int(words[1]))
        bisect.insort(leftList, int(words[0]))

# compute distance
for i in range(len(leftList)):
    distance = abs(leftList[i] - rightList[i])
    distanceList.append(distance)
    
print(sum(distanceList))

# PART 2
similarityScore = 0

# calculate similarity score
for num in leftList:
    similarityScore += num * rightList.count(num)

print(similarityScore)