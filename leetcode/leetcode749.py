def containVirus(isInfected):
    m = len(isInfected)
    n = len(isInfected[0])
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    # 遍历该区域中的每一个点，通过dfs判定每一个病毒区即将感染的大小，封锁即将感染最大面积的病毒区

    # 该方法用于获取从point出发的点扩散区大小
    def dfs(x, y, area):
        allCanInfected = 0
        area[x][y] = 2
        for i, j in direction:
            if 0 <= i + x < m and 0 <= j + y < n:
                if area[i + x][j + y] == 1:
                    allCanInfected += dfs(i + x, j + y, area)
                elif area[i + x][j + y] == 0:
                    allCanInfected += 1
        return allCanInfected

    # 该方法用于给从(x,y)出发的病毒区进行扩散
    def infecting(x, y, area):
        area[x][y] = 3
        for i, j in direction:
            if 0 <= i + x < m and 0 <= j + y < n:
                if area[i + x][j + y] == 1:
                    infecting(i + x, j + y, area)
                elif area[i + x][j + y] == 0:
                    area[i + x][j + y] = 3

    # 该方法用于给从(x,y)出发的病毒区进行封口
    def blockArea(x, y, area):
        area[x][y] = 4
        for i, j in direction:
            if 0 <= i + x < m and 0 <= j + y < n:
                if area[i + x][j + y] == 1:
                    blockArea(i + x, j + y, area)

    # 重置区域内容
    def inializeArea(area):
        for i in range(m):
            for j in range(n):
                if area[i][j] == 3 or area[i][j] == 2:
                    area[i][j] = 1

    # 首先，遍历各个病毒区，用一个列表存储每个病毒的出发点以及可能扩散的区域总数
    startLists = []

    for a in range(m):
        for b in range(n):
            if isInfected[a][b] == 1:
                # 存储病毒区的起始坐标以及可能扩散的大小
                startLists.append([a, b, dfs(a, b, isInfected)])

    inializeArea(isInfected)

    startLists = sorted(startLists, key=lambda s: s[2])
    print(startLists)
    # 以扩散区的大小进行排列
    res = 0
    while startLists:
        # 先封住最大一块区域
        cur = startLists.pop()
        blockArea(cur[0], cur[1], isInfected)
        res += cur[2]
        if startLists:
            tempStartLists = []
            # 剩下的区域扩散
            for x, y, z in startLists:
                if isInfected[x][y] != 4:
                    infecting(x, y, isInfected)
                    inializeArea(isInfected)
                    tempStartLists.append([x, y, dfs(x, y, isInfected)])

            # 以可能扩散的区域进行排序
            tempStartLists = sorted(tempStartLists, key=lambda s: s[2])

            # 因为扩散后，病毒区值为3，因此进行重置
            inializeArea(isInfected)
            startLists = tempStartLists

        else:
            break

    return res


# print(containVirus(isInfected=[[0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
#                                [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
#                                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#                                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#                                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#                                [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                                [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#                                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#                                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]]))

print(containVirus(isInfected=
                   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# print(containVirus(isInfected=[[0, 1, 0, 0, 0, 0, 0, 1],
#                                [0, 1, 0, 0, 0, 0, 0, 1],
#                                [0, 0, 0, 0, 0, 0, 0, 1],
#                                [0, 0, 0, 0, 0, 0, 0, 0]]))
#
# print(containVirus(isInfected=[[1, 1, 1, 0, 0, 0, 0, 0, 0],
#                                [1, 0, 1, 0, 1, 1, 1, 1, 1],
#                                [1, 1, 1, 0, 0, 0, 0, 0, 0]]))
#
# print(containVirus(isInfected=[[1, 1, 1],
#                                [1, 0, 1],
#                                [1, 1, 1]]))
