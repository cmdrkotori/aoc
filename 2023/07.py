#!/usr/bin/pypy3
from functools import cmp_to_key
from collections import defaultdict
lines = open('07.txt').read().strip().split('\n')
hands = [[list(h[0]),int(h[1])] for h in [l.split() for l in lines]]
power = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13 }
Part2 = False

def check_five(values):
    no_joker = [v for v in values if v != 'J'] if Part2 else values
    value_counts = defaultdict(lambda:0)
    for v in no_joker:
        value_counts[v]+=1
    if len(set(no_joker)) == 1:         #4444J,444JJ,44JJJ,4JJJJ
        return True
    if not Part2:
        return False
    if len(set(values)) == 1:           #JJJJJ
        return True
    else:
        return False

def check_four_of_a_kind(values):
    no_joker = [v for v in values if v != 'J'] if Part2 else values
    value_counts = defaultdict(lambda:0)
    for v in no_joker:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]: #23333
        return True
    if not Part2:
        return False
    if sorted(value_counts.values()) == [1,3]: #2333J
        return True
    if sorted(value_counts.values()) == [1,2]: #233JJ
        return True
    if sorted(value_counts.values()) == [1,1]: #23JJJ
        return True
    return False

def check_full_house(values):
    no_joker = [v for v in values if v != 'J'] if Part2 else values
    value_counts = defaultdict(lambda:0)
    for v in no_joker:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]: #22333
        return True
    if not Part2:
        return False
    if sorted(value_counts.values()) == [2,2]: #2233J
        return True
    return False

def check_three(values):
    no_joker = [v for v in values if v != 'J'] if Part2 else values
    value_counts = defaultdict(lambda:0)
    for v in no_joker:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,3]:
        return True
    if not Part2:
        return False
    if sorted(value_counts.values()) == [1,1,2]:
        return True
    if sorted(value_counts.values()) == [1,1,1]:
        return True
    else:
        return False

def check_two_pair(values):
    no_joker = [v for v in values if v != 'J'] if Part2 else values
    value_counts = defaultdict(lambda:0)
    for v in no_joker:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]: #23344
        return True
    else:
        return False

def check_one_pairs(values):
    no_joker = [v for v in values if v != 'J'] if Part2 else values
    value_counts = defaultdict(lambda:0)
    for v in no_joker:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,1,2]: #22345
        return True
    if not Part2:
        return False
    if sorted(value_counts.values()) == [1,1,1,1]: #J2345
        return True
    else:
        return False


def hand_type(h):
    if check_five(h):
        return 0
    if check_four_of_a_kind(h):
        return 1
    if check_full_house(h):
        return 2
    if check_three(h):
        return 3
    if check_two_pair(h):
        return 4
    if check_one_pairs(h):
        return 5
    return 6


def hand_type_pretty(h):
    if check_five(h):
        return '5'
    if check_four_of_a_kind(h):
        return '4'
    if check_full_house(h):
        return 'F'
    if check_three(h):
        return '3'
    if check_two_pair(h):
        return '2'
    if check_one_pairs(h):
        return '1'
    return '0'

def cmp_cards(h1,h2):
    for r in range(5):
        p1 = power[h1[r]]
        p2 = power[h2[r]]
        if p1 > p2:
            return -1
        if p1 < p2:
            return 1
    return 0

def cmp_hand(h1,h2):
    t1 = hand_type(h1[0])
    t2 = hand_type(h2[0])
    if t1 != t2:
        return t2 - t1
    return cmp_cards(h1[0],h2[0])

if Part2:
    power['J'] = 14

hands2 = hands
hands2.sort(key=cmp_to_key(cmp_hand))
print(sum([hands2[rank][1]*(rank+1) for rank in range(len(hands2))]))
