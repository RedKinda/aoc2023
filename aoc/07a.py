from collections import defaultdict


day = "07"
inp = open("input/{}.txt".format(day)).read()

# inp = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

CARDS = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")

# order of strengths is five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card


def get_counts(cards):
    counts = defaultdict(int)
    for card in cards:
        counts[card] += 1
    return list(sorted(counts.values(), reverse=True))


checks = (
    lambda cards: len(set(cards)) == 1,  # five of a kind
    lambda cards: len(set(cards)) == 2
    and cards.count(cards[0]) in (1, 4),  # four of a kind
    lambda cards: len(set(cards)) == 2
    and cards.count(cards[0]) in (2, 3),  # full house
    lambda cards: len(set(cards)) == 3 and get_counts(cards)[0] == 3,  # three of a kind
    lambda cards: len(set(cards)) == 3 and get_counts(cards)[0] == 2,  # two pair
    lambda cards: len(set(cards)) == 4,  # one pair
    lambda cards: len(set(cards)) == 5,  # high card
)


class Hand:
    def __init__(self, cards):
        self.cards = cards

        self.value = 0
        for i, check in enumerate(checks):
            if check(self.cards):
                self.value = i
                break

    def __gt__(self, other):
        if self.value == other.value:
            # compare cards in order
            for i in range(5):
                if CARDS.index(self.cards[i]) > CARDS.index(other.cards[i]):
                    return True
                elif CARDS.index(self.cards[i]) < CARDS.index(other.cards[i]):
                    return False

        return self.value > other.value

    def __repr__(self):
        return "<Hand {}>".format("".join(self.cards))


plays = []

for line in inp.splitlines():
    cards, bet = line.split(" ")
    plays.append((Hand(list(cards)), int(bet)))

# sort them
plays.sort(reverse=True)

res = 0

for ind, (hand, bet) in enumerate(plays):
    res += bet * (ind + 1)

print(res)
