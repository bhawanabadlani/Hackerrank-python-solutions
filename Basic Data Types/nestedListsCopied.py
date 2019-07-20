Report = []
lowest = 101
secondLowest = 102
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        if(score<lowest):
            secondLowest = lowest
            lowest = score
        elif(score<>lowest and score<secondLowest):
                secondLowest = score
        Report.append([name, score])
result = []
for item in Report:
if (item[1] == secondLowest):
        result.append(item[0])
result.sort()
for item in result:
        print(item)

