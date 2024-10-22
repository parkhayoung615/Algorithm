while(1):
    d,s = 0, int(input())
    if(s == 0): break
    for i in range(1, s + 1): d += i
    print (d)