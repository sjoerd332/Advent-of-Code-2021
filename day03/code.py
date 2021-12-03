#with open('test1.txt') as f:
with open('input.txt') as f:
    lines = f.readlines()
    values = [int(i.replace('\n',''),2) for i in lines]

gamma = 0
eps = 0
for i in range(len(lines[0])-1):
    n = 0
    p = 0
    for j in range(len(lines)):
        if values[j] & 2**i > 0:
            p = p + 1
        else:
            n = n + 1
    if p >= n:
        gamma = gamma + 2**i
    else:
        eps = eps + 2**i
        
print('ans 1: ' + str(gamma*eps))