import re 

#ユースケ・サンタマリアの名前定義
#ユースケ・サンタマリアの本名
realname ='中山祐介'
yusuke_santamaria = 'ユースケ・サンタマリア'
yusuke = 'ユースケ'
santamaria = 'サンタマリア'

char_yu ='ユ'
char_bou='ー'
char_su ='ス'
char_ke ='ケ'
char_dot='・'
char_sa ='サ'
char_n  ='ン'
char_ta ='タ'
char_ma ='マ'
char_ri ='リ'
char_a  ='ア'

#名前の文字数情報
#「ユースケ」の文字数
len_yusuke = 4
#「サンタマリア」の文字数
len_santamaria = 6
#「ユースケ・サンタマリア」の文字数
len_total = 11

inp_str =''




#パターン定義
#カタカナで〇ー〇〇・〇〇〇〇〇〇
kata = re.match( '[ア-ン]ー[ア-ン]{2}・[ア-ン]{6}',inp_str)
#カタカナで前方部分が〇ー〇〇で後方部分は問わない
kata_befor = re.match ('[ア-ン]ー[ア-ン]{2}・[ア-ン]+',inp_str)
#カタカナで前方部分が〇ー〇〇で後方部分は問わない
kata_after = re.match ('[ア-ン]+・[ア-ン]{wc_santamaria}',inp_str)
#文字列がカタカナでどっとで区切られていている
kata_dot = re.match ('[ア-ン]+・[ア-ン]+',inp_str)

#文字列が・で区切られている
dot = re.match ('\S+・\S+',inp_str)
#前方の文字列が4文字
dot_bf_4 = re.match ('\S{wc_yusuke}・\S+',inp_str)
#後方の文字列が6文字
dot_af_6 = re.match ('\S+・\S{wc_santamaria}',inp_str)
#〇ー〇〇・〇〇〇〇〇〇になっている(カタカナかどうかは問わない)
dot_4_6 = re.match ('\Sー\S{2}・\S{6}',inp_str)




