#with open('test1.txt') as f:
with open('input.txt') as f:
    lines = f.readlines()
    values = [int(i.replace('\n',''),2) for i in lines]
bits = len(lines[0])-1
gamma = 0
eps = 0
oxyCandidates = values
co2Candidates = values

# check ones and zeros
def checkOZ(values,bit):
    n = 0
    p = 0
    for j in range(len(values)):
        if values[j] & 2**bit > 0:
            p = p + 1
        else:
            n = n + 1
    return [p, n]

for i in reversed(range(bits)):
    [p,n] = checkOZ(values,i)
    if p >= n:
        gamma = gamma + 2**i
    else:
        eps = eps + 2**i
    
print('ans 1: ' + str(gamma*eps))

for i in reversed(range(bits)):
    [p,n] = checkOZ(oxyCandidates,i)
    if len(oxyCandidates) > 1:
        tmp = []
        for j in range(len(oxyCandidates)):
            if p >= n and oxyCandidates[j] & 2**i > 0:
                tmp.append(oxyCandidates[j])
            elif p < n and oxyCandidates[j] & 2**i == 0:
                tmp.append(oxyCandidates[j])
        oxyCandidates = tmp
        
for i in reversed(range(bits)):
    [p,n] = checkOZ(co2Candidates,i)
    if len(co2Candidates) > 1:
        tmp = []
        for j in range(len(co2Candidates)):
            if p < n and co2Candidates[j] & 2**i > 0:
                tmp.append(co2Candidates[j])
            elif p >= n and co2Candidates[j] & 2**i == 0:
                tmp.append(co2Candidates[j])
        co2Candidates = tmp

print('ans 2: ' + str(co2Candidates[0]*oxyCandidates[0]))