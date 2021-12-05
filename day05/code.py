with open('test1.txt') as f:
    N = 10
#with open('input.txt') as f:
    # N = 1000
    lines = f.readlines()
    values = [i.replace('\n','') for i in lines]

N = 10
map = [[0]*N for _ in range(N)]

def printMap():
    for i in range(N):
        print(map[i])

for line in values:
    #find start/end
    sx = int(line[:line.find(',')])
    sy = int(line[line.find(',')+1:line.find(' ->')])
    ex = int(line[line.find(' ->')+4:line[4:].find(',')+4])
    ey = int(line[line[4:].find(',')+4+1:])
    
    # sample points
    [sx,ex] = [sx,ex] if sx < ex else [ex,sx]
    [sy,ey] = [sy,ey] if sy < ey else [ey,sy]    
#    print(line)
    
    # fill map, non diagonal
    if(sx == ex or sy == ey):
        for x in range(N):
            for y in range(N):
                if x >= sx and x <= ex:
                    if y >= sy and y <= ey:
                        map[y][x] = map[y][x] + 1
    
# printMap()
dangerous = 0
for x in range(N):
    for y in range(N):
        if(map[y][x] >= 2):
            dangerous = dangerous +1
print('ans1 : ' + str(dangerous))