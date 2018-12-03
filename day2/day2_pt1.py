from collections import Counter

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

#print(only_thrice)
  
print(len(only_thrice) * len(only_twice))