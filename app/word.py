import re
from itertools import groupby
from functools import reduce

"""/**
* 最近在读英语短文小说，发现了不少生词，顺便记录了一下，然后就有了一下需求；
*
* 统计单词数据
* 需求：
* 1. 将所有生词按照字母排序
* 2. 按首字母分组统计生词个数 （获取生词数最高的前3组）
* 3. 找出所有没有音标的生词
* 4. 找出所有词组
*/"""


class Word(object):
    def __init__(self, spell, soundmark='', remark=''):
        self._spell = spell
        self._soundmark = soundmark
        self._remark = remark

    @property
    def spell(self):
        return self._spell

    @property
    def soundmark(self):
        return self._soundmark

    def __str__(self):
        return 'spell:%s, soundmark:%s remark:%s' % (self._spell, self._soundmark, self._remark)


def get_words():
    words = []
    with open('words.txt', 'r', encoding='utf-8') as f:
        regex = r'([\w\s]+)\s(\[.+?\])?(.+)'
        for line in filter(lambda l: len(l.strip()) > 0 and not l.strip().startswith('#'), f.readlines()):
            m = re.match(regex, line.strip())
            words.append(Word(m.group(1).strip(), m.group(2), m.group(3).strip()))
    return words


all_words = get_words()


# 需求1
def one():
    """将所有生词按照字母排序"""
    all_words.sort(key=lambda it: it.spell.upper())  # 替换了 all_words
    for s in all_words:
        print(s.spell)


def two():
    """2. 按首字母分组统计生词个数 （获取生词数最高的前3组)"""
    all_words.sort(key=lambda it: it.spell.upper())  # 替换了 all_words
    groupby_words = groupby(all_words, lambda x: x.spell[0].lower())
    dict = {}
    # 分组打印
    for s, lst in groupby_words:
        dict[s] = list(lst)
        print('%s: [%s]' % (s, reduce(lambda x, y: x + "," + y, map(lambda x: x.spell, dict[s]))))

    print("获取生词数最高的前3组")
    # print(sorted(dict.items(), key=lambda x: len(x[1]), reverse=True))
    for key, values in sorted(dict.items(), key=lambda x: len(x[1]), reverse=True)[0:3]:
        print(key + "," + str(len(values)))
        value = ', '.join(list(map(lambda x: x.spell, values)))
        print('====>%s: %s' % (key, value))

    # sort_list = sorted(dict.items(), key=lambda x:len(x.), reverse=True)
    # for i in sort_list[0:3]:
    #     print(i)


def three():
    """ 找出所有没有音标的生词 """
    filter_words = filter(lambda it:it.soundmark is None, all_words)
    for word in filter_words:
        print(word.spell)



def answer():
    # one()
    # two()
    three()


answer()
