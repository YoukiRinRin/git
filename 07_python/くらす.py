class MyClass:
    user_name = None
    age = None
    def say(self):
        print("名前:{0}、年齢:{1}".format(self.user_name,self.age))

user1 = MyClass()
user1.user_name = "山田"
user1.age = 20


user2 = MyClass()
user2.user_name = "前山田"
user2.age = 40

user1.say()
user2.say()

class Myclass2:
    fruits = []
    def __init__(self):
        print("コンストラクタが呼び出されました")
        self.fruits.append("パイナップル")
        self.fruits.append("メロン")
        self.fruits.append("いちご")

instance = Myclass2()
print(instance.fruits)


class Fish:
    def __init__(self,name,build="ほね",eyelids=False):
        self.name = name
        self.build = build
        self.eyelids = eyelids

    def swim(self):
        print("こちらの魚は泳ぎます。")
    def swim_back(self):
        print("こちらの魚はうしろにも泳ぎます")
    
class Medaka(Fish):
    pass

class kingyo(Fish):
    def __init__(self, name, build="ほね", eyelids=False):
        super().__init__(name, build=build, eyelids=eyelids)

        self.name='金魚ちゃん'+name+'だよ'
        self.build = build +'かな'
        self.eyelids = eyelids

class Cat(object):
    def __init__(self,name):
        self.name = name

class SuperCat(Cat):
    def __init__(self,name,function):
        super(SuperCat,self).__init__(name)
        self.function = function

class GodCat(SuperCat):
    def __init__(self, name, function,magic):
        super(GodCat,self).__init__(name, function)
        self.magic = magic
    def power(self):
        self.magic = 'マジックパワー！！'+self.function * self.magic

sample1 = Cat('ちゃちゃ')
sample2 = SuperCat('こん','飛ぶ')
sample3 = GodCat('みーな','潜る',5)
print(sample1.name)
print(sample2.name,sample2.function)
sample3.power()
print(sample3.name,sample3.magic)


class Employee:

    def __init__(self,first) -> None:
        pass


a = "Hello"
b = "world"

c=a+b
print( "%s+%s=%s" % ( a,b,c ) )

f=a*10
print(f)

d=format('%s %s'%(a,b))
print(d)

g=b.replace('or','OR')
print( g )

h = 'hello \n\n\n'



print(h)
i=h.strip()
print(i)

from datetime import date
from dateutil.relativedelta import relativedelta

d0 = date(1998,5,12)

d1 = date.today()
dy = relativedelta(d1,d0)

print(dy)

def age_calculator(d0,d1=date.today()):
    dy = relativedelta(d1,d0)
    return dy.years

age = age_calculator(d0,d1)

print(age)

import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta

def rand_birth(d1=date.today(),upper=100):
    year_now = d1.year

    rd = np.random.randint(1,upper+1)

    d0 = date(year_now - rd,1,1)

    d = np.random.ranfint(0,366)

    birthday = d0 + relativedelta(days=+d)

    age = age_calculator(birthday,d1=d1)

    return birthday,age

    
a = np.array([1,2,3])

print(a)
print(a.shape)

b = np.array(
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
)

print(b.shape)
print(b.ndim)
print(b.size)

a = np.zeros((3,4))

e = np.random.random((4,5))