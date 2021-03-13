# -*- coding:utf-8 -*-
import collections
# todo split 使用：
# todo sorted 使用：sorted(iterable, key=None),key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。

# index : 传入value 返回索引
# todo 如何实现洗牌 第11章 __setitem__

# 用来构建只有少量属性，但没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')
print(beer_card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # 初始化具名元组
        print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """__getitem__方法把[]操作给了._cards列表， 所以deck类支持切片操作， 同时也支持迭代"""
        return self._cards[position]

    def __repr__(self):
        """把对象用字符串的形式表达出来"""
        return "str of obj"


# --------------------------------------

deck = FrenchDeck()
print(deck)
print(len(deck))
# -------------------------------------

print(deck[0])
# ----------------------------------------
from random import choice

print(choice(deck))


# -----------排序------------------
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):  # doctest: +Ellipsis
    print(card)

"""
总结：
python的特殊方法是 为了给python解释器调用， 我们并不需要调用他们，也就是说没有my_object.__len__()
很多时候 特殊方法调用时隐式的，例外是__init__
"""