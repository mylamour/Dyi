# import os
# from secrets import SystemRandom
# from copy import deepcopy
#
#
# # 1、TM总数为49个， start为1， end为49
# # 2、【随机】选择一个位置K1, 依次划分 left 或 right 或者人工选择 left right. left=TM[:K1] right=TM[K1:]
# # 3、 从left 或 right 中随机或人工选择, left中选择一个随机数叫Unknown=do.randint(start,K1) 或者是right中选择一个随机数 do.randint(K1,end)记为S1, 然后S1=left.remove(Unknown)
# # 4、在S1中以4位长度进行【顺序4,3,2,1】切片得到m组数据 m = chunks(S1,4)
#
# # 第一种理解:
# # 第一遍： 不够5根的加到5根，超过5根的加到9根
# # [15]
# # A1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
# # B1: [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# # [1, 2, 3, 4][29]
# # [5, 6, 7][30,31]
# # [8, 9][32,33,34]
# # [10][35,36,37,38]
#
# # 5根或9根以外的合在一起, A1剩9 记为A2 B1剩11即为B2
# # 余下: [11, 12, 13, 14, 16, 17, 18, 19, 20]
# # 结果为 9
#
# # 第二遍： 不够4根的加到4根，超过4根的加到8根
# # A2: [11, 12, 13, 14, 16, 17, 18, 19, 20]
# # B2: [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# #
# # [11,12,13,14]
# # [16,17,18][39]
# # [19,20][40,41]
#
# # 结果为4
#
# # 第三遍: 不够4根的加到4根，超过4根的加到8根
# # B3: [42, 43, 44, 45, 46, 47, 48, 49]
# # 结果为8
#
# # 测试 第一变结果（长度）是 5 或 9 、 第二变 4 或 8 、 第三变 4 或 8
#
# # 4、5 为奇数（都是含一个4）
# # 8、9 为偶数（都是含二个4）
#
# # 步骤循环6次，获得18变。 每次三变成爻，六爻成卦，从初画起至上爻
# #
# # # 9，4，8
# # 一份为奇数（两份偶数） 为少阳  不变爻
# # 二份为奇数（一份偶数） 为少阴  不变爻
# # 三份为奇数 （没有偶数）为老阳  变爻
# # 三份为偶数 （没有奇数）为老阴  变爻
# def S(left, right):
#
#     yy = DOD.randint(YIN, YANG)
#
#     if yy == YIN:
#         flag = DOD.randint(START, len(left))
#
#         print("选择左边，左边位置拿出一份: {} \t".format(flag))
#         LEFT.remove(flag)
#
#         a = deepcopy(left)
#         b = deepcopy(right)
#
#     if yy == YANG:
#         flag = DOD.randint(K1 + 1, END)
#
#         print("选择右边，右边位置拿出一份: {} \t".format(flag))
#         RIGHT.remove(flag)
#
#         a = deepcopy(right)
#         b = deepcopy(left)
#
#     return a, b, flag
#
#
# def chunks(a, n):
#     t = []
#     for sp in list(reversed(range(1, n + 1))):
#         if a[:sp]:
#             t.append(a[:sp])
#             a = list(set(a) - set(a[:sp]))
#     # 4,3,2,1减去后剩下的放一起
#     if a:
#         t.append(a)
#
#     return t
#
#
# def L1_fixed(last, b):
#     if len(last) > 9:
#         print("超出9进行裁剪，裁剪后的L1", list(set(last) - set(last[9:])))
#         last = last[9:]
#
#     elif 5 < len(last) <= 9:
#         sp = b[: 9 - len(last)]
#         last.extend(sp)
#         print("超出5根不够9根，补充后的L1", last)
#         last = last[5:]
#
#     elif len(last) < 5:
#         sp = b[:5 - len(last)]
#         last.extend(sp)
#         print("不够5根，补充后的L1", last)
#     else:
#         print("FUCK ????")
#
#     return deepcopy(last), deepcopy(b)
#
#
# def L2_L3_fixed(last, b):
#     if len(last) > 8:
#         print("超出8进行裁剪，裁剪后的L2", list(set(last) - set(last[8:])))
#         last = last[8:]
#
#     elif 4 < len(last) <= 8:
#         sp = b[: 8 - len(last)]
#         last.extend(sp)
#         print("超出4根不够8根，补充后的L2", last)
#         last = last[5:]
#
#     elif len(last) < 4:
#         sp = b[:4 - len(last)]
#         last.extend(sp)
#         print("不够4根，补充后的L2", last)
#     else:
#         print("FUCK ????")
#
#     return deepcopy(last), deepcopy(b)
#
#
# START = 1
# END = 49
# YIN = 0
# YANG = 1
#
# STEP = 4
#
# TM = list(range(START, START + END))
#
# DOD = SystemRandom()
# K1 = DOD.randint(START, END)
#
# print("以此为界，左右分开。-> ", K1)
#
# LEFT = TM[:K1]
# RIGHT = TM[K1:]
#
# print("左为: ", LEFT)
# print("右为: ", RIGHT)
#
# A1 = A2 = A3 = []
# B1 = B2 = B3 = []
# C1 = C2 = C3 = []
# F1 = F2 = F3 = None
# G1 = G2 = G3 = None
#
# A1, B1, F1 = S(LEFT, RIGHT)
#
# print("这是A1:\t", A1)
# print("这是A1中取出的:\t", F1)
# print("这是B1:\t", B1)
#
# C1 = chunks(A1, STEP)
# print("这是C1:\t", C1)
#
# L1 = C1[-1] + [F1]
# print("这是C1和原来的数放在一起:\t", L1)
#
# LEFT, RIGHT = L1_fixed(L1, B1)
#
# print(LEFT,RIGHT)
# C2 = chunks(A2, STEP)
# print(C2)


#  Simple Version

# [5,9][4,8]