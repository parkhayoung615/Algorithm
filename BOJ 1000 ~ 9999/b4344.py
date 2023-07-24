for i in range(int(input())):
    data = list(map(int, input().split()))
    n = data[0]
    data.pop(0)
    tot = sum(data)/len(data)
    list1 = []
    for j in range(n):
        if tot < data[j]:
            list1.append(data[j])
    rou = round(len(list1) / len(data) * 100, 3)
    print ('%.3f%%' %rou)