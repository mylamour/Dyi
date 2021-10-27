import json
from secrets import SystemRandom


YIN = 0
YANG = 1
DOD = SystemRandom()
K1 = DOD.randint(YIN, YANG)

bagua = {
    '111': {'logo': '☰', 'text': '乾'},
    '011': {'logo': '☱', 'text': '兑'},
    '101': {'logo': '☲', 'text': '离'},
    '001': {'logo': '☳', 'text': '震'},
    '110': {'logo': '☴', 'text': '巽'},
    '010': {'logo': '☵', 'text': '坎'},
    '100': {'logo': '☶', 'text': '艮'},
    '000': {'logo': '☷', 'text': '坤'},
}

def gen():
    count = 0
    res = []
    for i in range(3):
        r = DOD.randint(YIN, YANG)
        count = count + 1
        if count == 1:
            if r == 1:
                res.append(5)

            if r == 0:
                res.append(9)
        elif r == 1:
            res.append(4)

        else:
            res.append(8)  # DOD.randint(YIN, YANG) == 1
    return res


def one(a):
    if a == 4 or a == 5:
        return '1'

    if a == 8 or a == 9:
        return '0'


def sone(rr):
    #  一份为奇数 为少阳  不变爻  ——
    #  二份为奇数 为少阴  不变爻  - -
    #  三份为奇数 为老阳  变爻  ——      要阳变阴
    #  三份为偶数 为老阴  变爻  — -    要阴变阳
    a, b, c = rr
    ms = {

        "m": None,
        "s": None
    }

    sb = one(a) + one(b) + one(c)

    if sb.count('1') == 0:
        ms['m'] = '0'
        ms['s'] = '1'

    if sb.count('1') == 1:
        ms['m'] = ms['s'] = '1'

    if sb.count('1') == 2:
        ms['m'] = ms['s'] = '0'

    if sb.count('1') == 3:
        ms['m'] = '0'
        ms['s'] = '1'

    return ms


def duanyi():
    m = ""
    s = ""
    c = 0

    for i in range(6):
        rr = gen()
        ms = sone(rr)
        if ms['m'] != ms['s']:
            c = c + 1

        m = m + ms['m']
        s = s + ms['s']

        print(rr)

    # 从初爻到上爻
    m = m[::-1]
    s = s[::-1]

    return m, s, c
# print(m,s)
# print("变爻数为: ", c)

# m_up = bagua[m[0:3]]
# m_down = bagua[m[3:6]]

# s_up = bagua[s[0:3]]
# s_down = bagua[s[3:6]]

# test = json.loads(open('./gua.json').read())
# for i in test['gua']:
#     if i['gua-xiang'] == m:
#         print(i)

#     if i['gua-xiang'] == s:
#         print(i)

# if c == 0:
#     # 无变爻， 查原卦
#     print("本卦为主")
#     print("上{}下{}".format(m_up['text'], m_down['text']))
#     print('{}\n{}'.format(m_up['logo'], m_down['logo']))

# if c == 1:
#     # 1个变爻, 查变爻有关占题答案
#     print("上{}下{}".format(m_up['text'], m_down['text']))
#     print('{}\n{}'.format(m_up['logo'], m_down['logo']))

#     print("变爻如下:")
#     print("上{}下{}".format(s_up['text'], s_down['text']))
#     print('{}\n{}'.format(s_up['logo'], s_down['logo']))

# if c == 2:
#     # 2个变爻，原卦为主，参看变卦
#     print("原卦为主")
#     print("上{}下{}".format(m_up['text'], m_down['text']))
#     print('{}\n{}'.format(m_up['logo'], m_down['logo']))

#     print("变卦如下:")
#     print("上{}下{}".format(s_up['text'], s_down['text']))
#     print('{}\n{}'.format(s_up['logo'], s_down['logo']))

# if c == 3:
#     # 原卦变卦互相参考
#     print("主卦变卦互相参考:")
#     print("上{}下{}".format(m_up['text'], m_down['text']))
#     print('{}\n{}'.format(m_up['logo'], m_down['logo']))

#     print("变卦如下:")
#     print("上{}下{}".format(s_up['text'], s_down['text']))
#     print('{}\n{}'.format(s_up['logo'], s_down['logo']))

# if c == 4 or c == 5:
#     # 以变卦为主，参看本卦
#     print("变卦为主:")
#     print("上{}下{}".format(s_up['text'], s_down['text']))
#     print('{}\n{}'.format(s_up['logo'], s_down['logo']))

#     print("本卦参考如下:")
#     print("上{}下{}".format(m_up['text'], m_down['text']))
#     print('{}\n{}'.format(m_up['logo'], m_down['logo']))

# if c == 6:
#     # 查看变卦有关占题答案
#     print("变卦为主:")
#     print("上{}下{}".format(s_up['text'], s_down['text']))

