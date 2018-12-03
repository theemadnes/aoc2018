with open('input.txt') as f:
    lines = f.read().splitlines()

base_frequency = 0

for x in lines:

    if x[0] == '+':
        #print('plus')
        base_frequency += int(x[1:])
    
    else:
        #print('minus')
        base_frequency -= int(x[1:])

    #print(base_frequency)

print(base_frequency)