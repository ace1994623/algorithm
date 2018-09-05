def a_star(data):
    puzzle = create_puzzle(data)



    puzzlelist = [puzzle]
    path = [puzzle]
    while True:
        step = 0
        for i in path:
            movelist = move(i)
            for j in movelist:
                if eval(j) not in puzzlelist:
                    step += 1
                    puzzlelist.append(eval(j))
            if h_manhaton(eval(j)) == 0:
                break
        path = puzzlelist[(len(puzzlelist) - step):]
        print(path)
        if h_manhaton(eval(j)) == 0:
            break
    return puzzlelist


def create_puzzle(data):
    puzzle = [[],[],[],[]]
    str = data.split(" ")
    for i in str:
        if str.index(i) < 4:
            puzzle[0].append(i)
        elif 4 <= str.index(i) < 8:
            puzzle[1].append(i)
        elif 8 <= str.index(i) < 12:
            puzzle[2].append(i)
        else:
            puzzle[3].append(i)
    return puzzle


def h_manhaton(data):
    result = 0
    for i in range(4):
        for j in range(4):
            if data[i][j] != "B":
                result += abs(i - int((int(data[i][j]) - 1) / 4)) + abs(j - ((int(data[i][j]) - 1) % 4))
    return result


def move(data):
    i = 0
    j = 0
    m = []
    n = []
    for d in range(4):
        if "B" in data[d]:
            j = data[d].index("B")
            i = d
            break

    # move up
    if i > 0:
        data[i][j],data[i - 1][j] = data[i - 1][j], data[i][j]
        m.append(str(data))
        data[i][j], data[i - 1][j] = data[i - 1][j], data[i][j]
    # move down
    if i < 3:
        data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
        m.append(str(data))
        data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
    # move left
    if j > 0:
        data[i][j], data[i][j - 1] = data[i][j - 1], data[i][j]
        m.append(str(data))
        data[i][j], data[i][j - 1] = data[i][j - 1], data[i][j]
    # move right
    if j < 3:
        data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]
        m.append(str(data))
        data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]

    for e in m:
        n.append(h_manhaton(eval(e)))

    if min(n) < h_manhaton(data):
        m = [m[n.index(min(n))]]
    return m


print(a_star("1 2 3 4 5 6 7 8 9 10 12 B 13 14 11 15"))
