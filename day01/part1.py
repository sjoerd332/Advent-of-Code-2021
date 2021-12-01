# with open('test.txt') as f:
with open('input.txt') as f:
    lines = f.readlines()
    values = [int(i.replace('\n','')) for i in lines]

tot = 0
for i in range(1,len(values)):
    if values[i] - values[i-1] > 0:
       tot = tot + 1

print('ans 1: ' + str(tot))

N = 3
window = []
oldWindow = []
tot = 0
for i in range(0,len(values)):
    window.append(values[i])
    if len(window) > N:
        window = window[1:]
    if len(oldWindow) >= N and sum(window) > sum(oldWindow):
            tot = tot + 1
    oldWindow = window.copy()

print('ans 2: '+ str(tot))
