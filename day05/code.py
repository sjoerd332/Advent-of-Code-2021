# with open('test1.txt') as f:
    # N = 10
with open('input.txt') as f:
    N = 1000
    lines = f.readlines()
    values = [i.replace('\n','') for i in lines]

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
    [ssx,eex] = [sx,ex] if sx < ex else [ex,sx]
    [ssy,eey] = [sy,ey] if sy < ey else [ey,sy]    
#    print(line)
    
    # fill map, non diagonal
    if(ssx == eex or ssy == eey):
        for x in range(ssx,eex+1):
            for y in range(ssy,eey+1):
                if x >= ssx and x <= eex:
                    if y >= ssy and y <= eey:
                        map[y][x] = map[y][x] + 1
    # diagonal
    if((sx != ex) and (sy != ey)):
        for x in range(min(sx,ex),max(sx,ex)+1):
            if (sx < ex and sy < ey) or (sx > ex and sy > ey):
                y = min(sy,ey) + x - min(sx,ex)
            else:
                y = max(sy,ey) - (x - min(sx,ex))
            map[y][x] = map[y][x] + 1
                    
if N == 10:
     printMap()
dangerous = 0
for x in range(N):
    for y in range(N):
        if(map[y][x] >= 2):
            dangerous = dangerous +1
print('ans1 : ' + str(dangerous))
