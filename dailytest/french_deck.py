#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/3 16:26
import collections

# 构建只有少数属性但没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    deck = FrenchDeck()
    print len(deck)
    print deck[0]

    # 随机抽取一张牌
    from random import choice
    print choice(deck)

    # 去前三张
    print deck[:3]