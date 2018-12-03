from collections import Counter

cnt = Counter()
frequency = 0

keep_going = True

while (keep_going):

    with open('input.txt') as f:
        lines = f.read().splitlines()

    for x in lines:

        if x[0] == '+':
            #print('plus')
            frequency += int(x[1:])
        
        else:
            #print('minus')
            frequency -= int(x[1:])

        cnt[frequency] += 1

        if cnt[frequency] == 2:

            keep_going = False
            print(frequency)
            exit



