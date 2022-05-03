str_inp = input('文字を入力してください')
str_paiza = 'paiza'


if str_inp == str_paiza:
    print('YES')
else:
    print('NO')

num_inp = int(input('数値を入力してください'))

if num_inp < 100:
    print('YES')
else:
    print('NO')


inp_A = int(input('A:数値を入力してください'))
inp_B = int(input('B:数値を入力してください'))
inp_C = int(input('C:数値を入力してください'))

AB = inp_A * inp_B

if AB <= inp_C:
    print('YES')
else:
    print('NO')

N = int(input('数列の長さを入力してください'))
A = []
flug_zero = 0
for ix in range(N):
    message_show = ix + ':数値を入力してください'
    A.append(int(input(message_show)))
    if A[ix] == 0:
        flug_zero = 1

if flug_zero == 0:
    print('YES')
else:
    print('NO')



