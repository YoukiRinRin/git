score_love = 0
HP = 1000

print('うんちっち:ハローうんちっちだよ！')

#day1
inp_com = input('今日は何する？　1:散歩2:家でゴロゴロ3:だまれボケカス')
if inp_com == '1':
    inp_com = input('今日の天気は？ 1:晴れ 2:曇り 3:雨')
    if inp_com == '1':
        print('天気がいいし良いね！')
        score_love =score_love + 500
        inp_com = input('分かれ道だ！どっちに曲がる？　1:右2:左')
        if inp_com == '1':
            print('ライオンが現れた！')
            score_love -= 250
        elif inp_com == '2':
            print('おいしいラーメン屋を見つけた！')
            score_love += 500
        
elif inp_com == '2':
    inp_com = input('今日の天気は？ 1:晴れ 2:曇り 3:雨')
    if inp_com == '3':
        print('こんな日は家でゆっくりするのがいいね！')
        score_love += 500
        inp_com = input('家で何しよっか　1:映画をみる 2:瞑想')
        if inp_com == '1':
            print('最悪のクソ映画だった')
            score_love -= 1000
        elif inp_com == '2':
            print('何もしないまま一日が終わった')
            score_love -= 500
elif inp_com == '3':
    score_love =score_love+ 1000

inp_com = ""

print(score_love)

#day2
if score_love < 1000:
    inp_com = input('今日は何する？　1:散歩2:家でゴロゴロ3:だまれボケカス')
elif score_love > 1000:
    inp_com = input('')


