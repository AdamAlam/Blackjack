from random import shuffle

faces = ["K", "Q", "J"]

full_deck = ["A", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "J", "Q", "K"] * 4


class Deck:
    def __init__(self, num_decks):
        self.stack = full_deck * num_decks

    def shuff(self):
        shuffle(self.stack)

    def take_card(self):
        return self.stack.pop()

    def __str__(self):
        return ', '.join(self.stack)


class my_Hand:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]
        self.flag = "hard"
        self.nums = [0, 0, 0, 0]

    def evaluate(self):
        for i in range(len(self.cards)):
            if self.cards[i] in faces:
                self.nums[i] = 10
            elif self.cards[i] == "A":
                self.flag = "soft"
                self.nums[i] = 11
            else:
                self.nums[i] = int(self.cards[i])
        return sum(self.nums)

    def soft_hard(self):
        if self.evaluate() > 21 and "A" in self.cards:
            self.nums[self.cards.index("A")] = 1
            self.flag = "hard"

    def __str__(self):
        return ' '.join(self.cards)


deck = Deck(4)
deck.shuff()
deck.shuff()
deck.shuff()
print((deck))
print()

myhand = my_Hand(deck.take_card(), deck.take_card())
print(str(myhand))
print(myhand.evaluate())
