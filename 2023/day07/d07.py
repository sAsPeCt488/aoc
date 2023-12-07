from enum import Enum
from typing import List
from collections import Counter

with open('07_example.txt', 'r') as f:
    hands = [x.split(" ") for x in [line.strip() for line in f.readlines() if line.strip()]]

PART1_EXAMPLE_ANSWER = 6440
PART2_EXAMPLE_ANSWER = 5905

class Order(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Card(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


CARD_FACE_MAP = {'T':Card.TEN, 'J':Card.JACK, 'Q':Card.QUEEN, 'K':Card.KING, 'A':Card.ACE}


def transform_hand(hand: List[List[str]]):
    cards, bid = hand
    cards_values = []
    for c in cards:
        if c in CARD_FACE_MAP:
            cards_values.append(CARD_FACE_MAP[c])
        else:
            cards_values.append(Card(int(c)))

    return Hand(cards_values, int(bid))



class Hand():

    def __init__(self, cards: List[Card], bid: int, joker_mode = False):
        self.cards = cards
        self.bid = bid
        self.joker_mode = False
        self.classify_hand()
        
    def _count_pairs_sets(self, counter):
        pairs = 0
        sets = 0
        for card, count in counter.items():
            if self.joker_mode and card == Card.JACK:
                continue

            if count == 2:
                pairs += 1

            if count == 3:
                sets += 1
        return pairs, sets

    def classify_hand(self):

        self.rank = Order.HIGH_CARD
        counts = Counter(self.cards)
        pairs, sets = self._count_pairs_sets(counts)
        
        joker_counts = dict(counts).get(Card.JACK, 0)

        if any([count == 4 for _, count in counts.items()]):
            self.rank = Order.FOUR_OF_A_KIND
        elif any([count == 5 for _, count in counts.items()]):
            self.rank = Order.FIVE_OF_A_KIND


        if self.rank == Order.HIGH_CARD:
            if pairs == 1:
                self.rank = Order.ONE_PAIR

            if self.rank == Order.ONE_PAIR and sets == 1:
                self.rank  = Order.FULL_HOUSE
            elif sets == 1:
                self.rank  = Order.THREE_OF_A_KIND

            if pairs == 2:
                self.rank  = Order.TWO_PAIR

        if self.joker_mode and joker_counts:
            for i in range(joker_counts):

                if self.rank == Order.FIVE_OF_A_KIND:
                    break

                match self.rank:
                    case Order.ONE_PAIR:
                        self.rank = Order.THREE_OF_A_KIND
                    case Order.TWO_PAIR:
                        self.rank = Order.FULL_HOUSE
                    case Order.FULL_HOUSE:
                        self.rank = Order.FOUR_OF_A_KIND
                    case Order.THREE_OF_A_KIND:
                        self.rank = Order.FOUR_OF_A_KIND
                    case _:
                        self.rank = Order(self.rank.value + 1)

    def __gt__(self, other):
        if isinstance(other, Hand):
            if self.rank.value > other.rank.value:
                return True
            
            elif self.rank.value == other.rank.value:

                for i in range(len(self.cards)):
                    if self.joker_mode and self.cards[i] == Card.JACK:
                        if other.cards[i] != Card.JACK:
                            return False
                    if self.joker_mode and other.cards[i] == Card.JACK:
                        if self.cards[i] != Card.JACK:
                            return True

                    if self.cards[i].value == other.cards[i].value:
                        continue

                    if self.cards[i].value > other.cards[i].value:
                        return True
                    else:
                        return False

            return False

normal_hands = []

for hand in hands:
    normal_hand = transform_hand(hand)
    normal_hands.append(normal_hand)

sorted_hands = sorted(normal_hands)

part1 = 0
for i, hand in enumerate(sorted_hands):
    part1 += (i + 1) * hand.bid

joker_hands = []
for hand in normal_hands:
    hand.joker_mode = True
    hand.classify_hand()
    joker_hands.append(hand)

sorted_joker_hands = sorted(joker_hands)

part2 = 0
for i, hand in enumerate(sorted_joker_hands):
    part2 += (i + 1) * hand.bid

assert part1 == PART1_EXAMPLE_ANSWER, f'Wrong Part 1 answer: {part1} expected {PART1_EXAMPLE_ANSWER}'
assert part2 == PART2_EXAMPLE_ANSWER, f'Wrong Part 2 answer: {part2} expected {PART2_EXAMPLE_ANSWER}'

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

    



    