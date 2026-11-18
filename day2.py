scores = [117, 80, 203, 95, 150]
overscores=[]

for i in scores:
    if i>=100:
        overscores.append(i)

overscores=sorted(overscores)

for i in overscores:
    print(f"{i}점 - 통과")


arr = [3,1,4]
arr.append(5)
print(len(arr), sum(arr), max(arr))
for x in arr:
    print(x)

n= int(input())
while n > 0:
    print(n, end=" ")
    n -= 1