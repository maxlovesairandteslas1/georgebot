import datetime
x = datetime.datetime.now()
x = x.strftime('%j')
x = int(x)-1
with open('status1.txt') as f:
    lines = f.read().splitlines()
statusfinal = lines[x]

print(statusfinal)