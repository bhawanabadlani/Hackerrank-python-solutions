Report = []
individualList = []
if __name__ == '__main__':
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        individualList = [name, score]
        Report.append(individualList)
lowest = Report[0][1]
for item in Report:
    if(lowest>item[1]):
        lowest = item[1]
#print(lowest)
secondLowest = Report[0][1]
result = []
for item in Report:
    if((secondLowest==lowest or item[1]<secondLowest) and item[1] != lowest):
        secondLowest = item[1]
#print(secondLowest)
for item in Report:
    if(item[1] == secondLowest):
        result.append(item[0])
result.sort()
for item in result:
        print(item)

