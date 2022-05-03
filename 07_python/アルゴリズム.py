def linear_search(data,value):
    for i in range(len(data)): 
        if data[i] == value:
            return i
    return -1


data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(linear_search(data, 21))

find_data = input('数値を入力してください')

try:
    find_data = int(find_data)
except Exception as e:
    print(e)


if linear_search(data,21) == -1:
    print("入力された値は見つかりませんでした")
else:
    print(linear_search(data, 21))