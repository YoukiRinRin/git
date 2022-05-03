import re
def checkMatch(msg,pat):
    pattern = re.compile(pat)
    result = pattern.match
    if result:
        print(result.group(0))
    else:
        print('Don\'matched')

    checkMatch('東京都港区赤坂',r'東京.')
    checkMatch('東京都港区赤坂',r'港.')