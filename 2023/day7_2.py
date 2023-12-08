from collections import Counter
from operator import countOf


replacer = {'A': '>', 'K': '=', 'Q': '<', 'J': '1', 'T': ':'}
hands = [{}, {}, {}, {}, {}, {}, {}]

def max_no_jolly(d):
    res = 0
    for k, v in d.items():
        if k != '1':
            res = max(res, v)
    return res


with open("2023/input.txt", "r") as f:
    for line in f:
        for k, v in replacer.items():
            line = line.replace(k, v)
        card, bid = line[:5], int(line[6:])
        counter = Counter(card)
        jollies = counter['1']
        if len(counter) == 1 or max_no_jolly(counter) + jollies == 5:
            hands[0][card] = bid
        elif 4 in counter.values() or max_no_jolly(counter) + jollies == 4:
            hands[1][card] = bid
        elif (3 in counter.values() and 2 in counter.values()) or (countOf(counter.values(), 2) == 2 and jollies == 1):
            hands[2][card] = bid 
        elif 3 in counter.values() or max_no_jolly(counter)+ jollies == 3:
            hands[3][card] = bid
        elif countOf(counter.values(), 2) == 2:
            hands[4][card] = bid
        elif countOf(counter.values(), 2) == 1 or jollies == 1:
            hands[5][card] = bid
        else:
            hands[6][card] = bid

for i in range(len(hands)):
    hands[i] = dict(sorted(hands[i].items()))


    
rank = 1
ans = 0
for d in hands[::-1]:
    for k, v in d.items():
        ans += v * rank
        rank += 1
print(ans)

        