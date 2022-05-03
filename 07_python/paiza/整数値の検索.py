N = int(input('数列の要素数を入力してください'))
A = []
X = int(input('検索したい値を入力してください'))

order_find = 0

for ix in range(N):
    message_show = ix + ':数値を入力してください'
    A.append(int(input(message_show)))
    
for ix in range(N):
    if A[ix] == X:
