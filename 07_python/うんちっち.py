print('うんちっちは今日も元気')


unchicch_HP = 0
unchicch_unco_point = 0
unchicch_shokumotu_point = 0
amount_unco = 0

inp_action = int(input('何をする？1:ご飯をあげる 2；昼寝をする 3:うんこをする'))

food = {1:'チャーハン',2:'ラーメン',3:'サラダ'}
HP = {}
unco = {}
bad = {}


def effect_food(HP,unco,bad):
    unchicch_HP += HP
    unchicch_shokumotu_point += unco
    unchicch_unco_point += bad



if inp_action == 1:
    food_message = '何を上げる？' + food
    inp_food = int(food_message)
    effect_food(food[inp_food],unco[inp_food],bad[inp_food])
  

if unchicch_HP == 10:
    print('進化')
if unchicch_unco_point == 10:
    print('gameover')
if unchicch_shokumotu_point == 10:
    print('うんちぶりぶり')


    #if inp_food