# Part 1

with open("Day7.txt", "r") as file:
    lines = file.readlines()

from collections import Counter

strength = {"A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}

def cards_in_hand(hand):
    cards = Counter(hand)
    return cards

def is_five_of_a_kind(cards):
    return 5 in cards.values()

def is_four_of_a_kind(cards):
    return 4 in cards.values()

def is_full_house(cards):
    return 3 in cards.values() and 2 in cards.values()

def is_three_of_a_kind(cards):
    return 3 in cards.values() and 1 in cards.values()

def is_two_pair(cards):
    return list(cards.values()).count(2) == 2

def is_one_pair(cards):
    return list(cards.values()).count(2) == 1 and list(cards.values()).count(1) == 3

def is_high_card(cards):
    return all(num == 1 for num in cards.values())

def hand_strength_parameters(hand):
    cards = cards_in_hand(hand)
    return [is_five_of_a_kind(cards), is_four_of_a_kind(cards), is_full_house(cards), is_three_of_a_kind(cards),
            is_two_pair(cards), is_one_pair(cards), is_high_card(cards)]

def compare_equal_hand(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if strength[card1] > strength[card2]:
            return 1
        elif strength[card2] > strength[card1]:
            return -1
    return 0
        
def compare(hand1, hand2):
    hand1_strength = hand_strength_parameters(hand1)
    hand2_strength = hand_strength_parameters(hand2)

    for s1, s2 in zip(hand1_strength, hand2_strength):
        if s1 and not s2:
            return 1
        elif not s1 and s2:
            return -1
        
    return compare_equal_hand(hand1, hand2)
        

cards = {}
for line in lines:
    parts = line.split(" ")
    hand = parts[0]
    score = int(parts[1])
    cards[hand] = score

from functools import cmp_to_key

temp_keys = list(cards.keys())
# temp_keys.sort(cmp=compare, reverse=True)
sorted(temp_keys, key=cmp_to_key(compare), reverse=True)
sorted_cards = {i: cards[i] for i in temp_keys}

total_score = 0

for rank, card in enumerate(sorted_cards.keys()):
    total_score += (sorted_cards[card] * (rank + 1))

print(total_score)