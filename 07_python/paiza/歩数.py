d = int(input('歩いた距離を入力してください(km)'))
s = int(input('あなたの歩幅を入力してください(cm)'))


d_cm = d // 100000
print(d_cm)
steps = d_cm // s 
print(steps)
print('あなたの歩数は',steps,'です')