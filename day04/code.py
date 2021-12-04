import csv

#with open('test1.txt') as f:
with open('input.txt') as f:
    lines = f.readlines()
    values = list(csv.reader(lines))

class board:
    def __init__(self,nrs):
        self.nrs = nrs
        self.ticks = [[0]*len(nrs[0]) for _ in range(len(nrs))]
        self.rb = [0]*len(nrs[0]) # is a column of row bingo status
        self.cb = [0]*len(nrs)    # is a row of column bingo status
        self.bingo = False

    def checkRowBingo(self):
        anyBingo = False
        for j in range(len(self.nrs)):
            bingo = True
            for i in range(len(self.nrs[j])):
                bingo = bingo and self.ticks[j][i]
            if bingo:
                self.rb[j] = 1
                anyBingo = True
                self.bingo = True
        return anyBingo

    def checkColBingo(self):
        anyBingo = False
        for j in range(len(self.nrs[0])):
            bingo = True
            for i in range(len(self.nrs)):
                bingo = bingo and self.ticks[i][j]
            if bingo:
                self.cb[j] = 1
                anyBingo = True
        return anyBingo

    def	checkBingo(self):
        bingo = False
        bingo = self.checkRowBingo()
        bingo = bingo or self.checkColBingo()
        return bingo
        
    def checkNrs(self,nr):
        for i in range(len(self.nrs)):
            for j in range(len(self.nrs[0])):
                if self.nrs[i][j] == nr:
                    self.ticks[i][j] = 1
    
    def playTurn(self,nr):
        self.checkNrs(nr)
        return self.checkBingo()
        
    def calcScore(self):
        score = 0
        for i in range(len(self.nrs)):
            for j in range(len(self.nrs[0])):
                score = score + (1-self.ticks[i][j])*self.nrs[i][j]
        return score

class game:
    def __init__(self,values):
        self.drawSeq = values[0]
        
        start = 0
        stop = 0
        for i in range(len(values)):
            if len(values[i]) == 0 and start > 0 and stop == 0:
                stop = i
                break
            if len(values[i]) == 0 and start == 0:
                start = i
        boardSize = stop-start-1
        self.boards = []
        
        i = 0
        while i < len(values):
            if len(values[i]) > 0 and len(values[i-1]) == 0:
                bv = []
                for j in range(boardSize):
                    row = values[i+j][0]
                    r = row.split()
                    for k in range(len(r)):
                        r[k] = int(r[k])
                    bv.append(r)
                self.boards.append(board(bv))
            i = i + 1

    def play(self):
        ans1 = 0
        self.bingos = []
        print('nrs: ')
        for nr in self.drawSeq:
            print(nr + ', ')
            nr = int(nr)
            
            for board in range(len(self.boards)):
                bingo = self.boards[board].playTurn(nr)
                if bingo:
                    score = nr * self.boards[board].calcScore()
                    if ans1 == 0:
                        ans1 = score
                    if board not in [b[0] for b in self.bingos]:
                            self.bingos.append([board, score])
                            print('nr: ' + str(nr) + '\tboard: '+ str(board) + '\tans1: ' + str(score))
        ans2 = self.bingos[-1][1]
        return [ans1, ans2]
        
game1 = game(values)
[a1, a2] = game1.play()
        
        
        
        
        
        
        
        
        
        
        
        
        
        

