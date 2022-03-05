N = int(input())
F = input().split(" ")
P = int(input())
AB = [input().split(" ") for j in range(P)]

newAB = []
for p1 in AB:
    new = []
    for p2 in AB:
        if (p1[0] in p2 or p1[1] in p2) and p1[0] not in new and p1[1] not in new:
            new += [int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])]
    if new:
        newAB.append(list(set(new)))

result = []
for ab in newAB:
    temp = []
    for idx in ab:
        temp.append(int(F[idx-1]))
    result.append(sum(temp))
print(max(result))
