from collections import Counter
import itertools

with open('input.txt') as f:
        lines = f.read().splitlines()

only_twice = []
only_thrice = []

for line in lines:

    cnt_2 = Counter()

    for letter in line:

        cnt_2[letter] += 1

    for val in cnt_2.values():

        if val == 2:

            only_twice.append(line)
            break

for line in lines:

    cnt_3 = Counter()

    for letter in line:

        cnt_3[letter] += 1

    for val in cnt_3.values():

        if val == 3:

            only_thrice.append(line)
            break

off_by_one = []

#for pair in zip(only_thrice, only_twice):
#
#    print(pair)

# join the data sets 

for thrice in only_thrice:

    for twice in only_twice:

        i = 0
        off_by_n = 0

        for x in thrice:

            if thrice[i] == twice[i]:

                pass

            else:

                off_by_n += 1

            i += 1

        if off_by_n == 1:

            off_by_one.append(thrice)
            print(twice)
            print(thrice)

print(off_by_one)












#print(only_thrice)
  
#print(len(only_thrice) * len(only_twice))

# get the union of the boxes

#candidates = list(set().union(only_thrice,only_twice))

#print(candidates)
#print(len(candidates))
