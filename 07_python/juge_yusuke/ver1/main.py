import re
import pattern as pt
import match as ma
import check_function as cf
import large_tone as lt


inp_str = input('文字列を入力してね')

char_list = list(inp_str)

regex_hira = '[\u3041-\u309F]'
regex_kata = '[\u30A1-\u30FF]'
result_hira =''
result_kata = ''

list_boin = []


print(char_list)

for i in range(len(char_list)):       
    result_hira = re.match(regex_hira,char_list[i])
    result_kata = re.match(regex_kata,char_list[i])

    if result_hira:
            list_boin.append(lt.hira[char_list[i]])
    elif result_kata:
            list_boin.append(lt.kata[char_list[i]])





score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score_total = 0

#文字数が一致するかどうか
if len(inp_str) == pt.len_total:
    print('a')
    #文字数が一致し、かつ文字がドットで区切られている
    cf.check_dot
else:
    if cf.check_dot == 'a':
        score_total += score1
    elif cf.check_dot == 'b':
        score_total += score2
    elif cf.check_dot == 'c':
        score_total += score3










#〇〇〇〇・〇〇〇〇〇〇の場合







print(inp_str+'のユースケ・サンタマリアっぽさは'+score_total+'点です。')
