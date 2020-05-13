#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/29 16:56
import collections
import random


# 构建只有少数属性但没有方法的对象
Card = collections.namedtuple('Card', ['Rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    # card_obj = Card['6', 'diamonds']
    deck_obj = FrenchDeck()
    print len(deck_obj)
    choice = random.choice(deck_obj)
    print choice
    print deck_obj[1::2]
    # 反向迭代
    for card in reversed(deck_obj):
        print card

    # 排序
    for card in sorted(deck_obj, key=spades_high):
        print card
