class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('[ INFO ] 오브젝트가 생성되었습니다.')

    def __str__(self):
        return f'{self.lastname}, {self.firstname}'

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def __str__(self):
        return f'{super().__str__()}, {self.graduationyear}'

    def say(self):
        print('벌써 집에 가고싶어 ')

y = Student('JIEUN', 'LEE', 2026)
print(y)
y.say()
