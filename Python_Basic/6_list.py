list = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(0)
    list.append(temp)

dir = 0 # 0: right, 1: down, 2: left, 3: up
now_i, now_j = 0, 0

for i in range(1, 26):
    list[now_i][now_j] = i
    if dir == 0:
        if now_j == 4 or list[now_i][now_j+1] != 0:
            dir = 1
            now_i += 1
        else:
            now_j += 1
    elif dir == 1:
        # TODO
        pass
    elif dir == 2:
        # TODO
        pass
    elif dir == 3:
        # TODO
        pass

for i in range(5):
    for j in range(5):
        print("%2d" % list[i][j], end=" ")
    print()
        


        
