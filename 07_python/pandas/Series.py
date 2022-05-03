import pandas as pd
s = pd.Series([10,20,30])
s2 = pd.Series([1,2,3,4],index=['a','b','c','d'])
s_dic = pd.Series({'a':1,'b':2,'c':3})
print(s)
print(s2)
print(s_dic)

print('s2[a]',s2['a'])
print('s2.a',s2.a)

print('s+10',s+10)
print('s-10',s-10)
print('s/10',s/10)
print('s*10',s*10)

s_1 = pd.Series([1,2,3,4,],index=['a','b','c','d'])
s_2 = pd.Series([1,2,3,4,],index=['a','b','c','d'])

print('s_1 + s_2',s_1 + s_2)
print('s_1 - s_2',s_1 - s_2)
print('s_1 * s_2',s_1 * s_2)
print('s_1 / s_2',s_1 / s_2)
print('s_1 > s_2',s_1 > s_2)
print('s_1 < s_2',s_1 < s_2)