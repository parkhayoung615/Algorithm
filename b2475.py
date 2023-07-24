o, t, h, f, v = map(int, input().split(" "))
r = (o*o)+(t*t)+(h*h)+(f*f)+(v*v)
print(r % 10)