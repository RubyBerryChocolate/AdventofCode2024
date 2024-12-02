safeCounter = 0
dampenedCounter = 0

def check(list):
    difference = [list[i+1] - list[i] for i in range(len(list) - 1)]
    absDifference = [abs(item) for item in difference]
    if sorted(list) == list or sorted(list, reverse=True) == list:
            if max(absDifference) <= 3 and min(absDifference) > 0: return True
            else: return False

with open('input.txt') as file:
    for rawLine in file:
        numbers = rawLine.split(' ')
        line = []
        for i in numbers:
            line.append(int(i))

        #part 1
        if check(line): safeCounter += 1
   
        #part2
        if any(check(line[:i] + line[i+1:]) for i in range(len(line))): dampenedCounter += 1
        
        # for i in range(len(line)):
        #     copyLine = line.copy()
        #     del copyLine[i]
        #     if sorted(copyLine) == copyLine or sorted(copyLine, reverse=True) == copyLine:
        #         copyDifference = [copyLine[j+1] - copyLine[j] for j in range(len(copyLine) - 1)]
        #         absCopyDifference = [abs(item) for item in copyDifference]
        #         if max(absCopyDifference) <= 3 and min(absCopyDifference) > 0:
        #             dampenedCounter += 1
        #             break

    print(safeCounter)
    print(dampenedCounter)