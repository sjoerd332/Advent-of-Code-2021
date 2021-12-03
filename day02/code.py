#with open('test1.txt') as f:
with open('input.txt') as f:
    lines = f.readlines()
    #values = [int(i.replace('\n','')) for i in lines]

class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
    
    def step(self, cmd):
        if cmd.find('forward') > -1:
            cnt = int(cmd.replace('forward ',''))
            self.horizontal = self.horizontal + cnt
        elif cmd.find('up') > -1:
            cnt = int(cmd.replace('up ',''))
            self.depth = self.depth - cnt
        elif cmd.find('down') > -1:
            cnt = int(cmd.replace('down ',''))
            self.depth = self.depth + cnt
    
    def step2(self,cmd):
        if cmd.find('forward') > -1:
            cnt = int(cmd.replace('forward ',''))
            self.horizontal = self.horizontal + cnt
            self.depth = self.depth + self.aim * cnt
        elif cmd.find('up') > -1:
            cnt = int(cmd.replace('up ',''))
            self.aim = self.aim - cnt
        elif cmd.find('down') > -1:
            cnt = int(cmd.replace('down ',''))
            self.aim = self.aim + cnt

    def area(self):
        return self.depth * self.horizontal
        
s = Submarine()
s2 = Submarine()
for i in lines:
    s.step(i)
    s2.step2(i)

print('ans 1: ' + str(s.area()))
print('ans 2: ' + str(s2.area()))