import re
def checkMatch(msg,pat):
    pattern = re.compile(pat)
    result = pattern.fullmatch(msg)
    if result:
        print(result.group(0))
    else:
        print('Don\'t matched')

    checkMatch('東京都赤坂',r'東.*区')

    checkMatch('東京都赤坂',r'東.*坂')
    

