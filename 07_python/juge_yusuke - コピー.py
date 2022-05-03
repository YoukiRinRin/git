import re
score_yusuke = 0 
get_str = input('文字列を入力してね')


pattern_yusuke = '[ア-ン]ー[ア-ン]{2}・[ア-ン]{6}'

result = re.match(pattern_yusuke,get_str)

if result:
    print('ユースケ・サンタマリアっぽい')
elif get_str == '中山祐介':
    print('それはユースケ・サンタマリアの本名です。')

else:
    print('ユースケ・サンタマリアっぽくない')