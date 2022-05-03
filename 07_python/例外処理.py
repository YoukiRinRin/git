try:
    a = 100/0
except Exception as e:
    print(e)
finally:
    print("終了")

class TestException(Exception):
    pass
def calc1(a):
    if a == 0:
        raise TestException('独自例外')
    return

a = 0

try:
    calc1(a)
except TestException as e:
    print(e)

finally:
    pass