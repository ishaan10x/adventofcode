import bisect

# PART 1

# fields
reports = []
numValid = 0

# read in reports as int list
with open('C:\\Users\\Ishaan\\myprojects\\adventofcode\\2024\\python\\day_2\\input.txt', 'r') as file:
    for line in file:
        reports.append([int(value) for value in line.split()])

# function to determine if a report is valid
def isValid(report):
    if (report[1] - report[0] > 0):
        polarity = 1
    else:
        polarity = -1
    
    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]

        # check polarity is consistent
        if (difference * polarity < 0):
            return False

        # check if change is gradual
        if abs(difference) < 1 or abs(difference) > 3:
            return False
    
    # every number is fine this report is valid
    return True

# check each report for validity
for report in reports:
    if (isValid(report)):
        numValid += 1

# print result
print(numValid)

# PART 2
num_valid_dampened = 0

def is_valid_dampened(report):
    if isValid(report):
        return True
    else:
        # brute force removal of each level and check validity
        for i in range(len(report)):
            if isValid(report[:i] + report[i+1:]):
                return True
    return False

for report in reports:
    if (is_valid_dampened(report)):
        num_valid_dampened += 1

print(num_valid_dampened)
