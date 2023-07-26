# !밀비 급일

while(1):
    c = (input())
    if(c == 'END'):
        break
    print(c[::-1])


# # 이렇게 했을 땐 안 됐음 눈물만 난다 ,,
# while(1):
#     c = list(input())
#     if(c == 'END'):
#         break
#     for i in reversed(c):
#         print(i, end='')