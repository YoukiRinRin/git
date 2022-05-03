import re
print('うんこ算を始めます')

unco1 = ''
unco2 = ''

unco = 'うんこ'

pattern_unco = '^うんこ'
pattern_num_unco = '\dうんこ'

unco1_count = unco1.count(unco)
unco2_count = unco2.count(unco)

num_unco1 = 0
num_unco2 = 0

while(1):
    unco1 = input('最初のうんこを入力してください')
    if re.match(pattern_unco,unco1):
        unco1_count = unco1.count(unco)
        num_unco1 = unco1_count
        break
    elif re.match(pattern_num_unco,unco1):
        if re.match(pattern_num_unco,unco1):
            num_unco1=int(unco1[0])
        break
    else:
        print('入力が間違っています')


while(1):
    unco2 = input('次のうんこを入力してくしてください')
    if re.match(pattern_unco,unco2):
        unco2_count = unco2.count(unco)
        num_unco2 = unco2_count
        break
    elif re.match(pattern_num_unco,unco2):
        if re.match(pattern_num_unco,unco2):
            num_unco2=int(unco2[0])
        break
    else:
        print('入力が間違っています')


    
for ix in range(num_unco1 + num_unco2):
    print(unco)    
        