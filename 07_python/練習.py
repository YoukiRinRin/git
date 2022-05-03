x = 1
y = "desktop"
mydict = {x:y}
print(mydict)


mydict = {"JP":"Japan","DE":"Germany","FR":"France"}

print(mydict["DE"])
print(mydict["FR"])
print(mydict["JP"])

key1 = "JP"
print("キー:"+key1+"、値:"+mydict[key1])

key2 = "FR"
print("キー:"+key2+"、値:"+mydict[key1])
key3 = ""

Key3 = input('DEを入力してね')
print(mydict.get(key3))

Key3 = input('ENを入力してね')
print(mydict.get(key3))

Key3 = input('キーを入力してね　JP FR DE')
print(mydict.get(key3),"うんちー！")

colorlist = ["Blue","Red","Green","While","Black"]
print("要素数は"+str(len(colorlist))+"です。")

mydict2 ={"A":"apple","L":"Lemon","O":"Orenge"}
print(mydict2)
del mydict2["L"]
print(mydict2)
del mydict2["p"]

val = mydict2.pop("L")
print(mydict2)
print(val)