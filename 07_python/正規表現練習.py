import re

target ='apple and orange'
pattern = re.compile(r'a...e')

result = pattern.search(target)

print(result)

pattern = re.compile(r'a.{3}e')
result = pattern.search(target)

if result:
    print(result.group())

pat = 'abc'

pat = 'png$'
pat = '\\w'

pat = r'\\w'

filename = 'apple.png'
pattern = re.compile(r'png$')

result = pattern.search(filename)

if result :
    print('パターンにマッチします')
else:
    print('パターンにマッチしません')

def checkMatch(msg,pattern):
    result =  pattern.serch(msg)
    if result:
        print(result.group(0))
    else:
        print('Don\'t matched')

pattern = re.compile(r'apple')

checkMatch('lemon,apple,peach',pattern)

checkMatch('grapes,cherry',pattern)

