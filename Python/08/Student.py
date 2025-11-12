from Person import Person

class Student(Person):

    def study(self):
        print('공부 하기 싫어 어ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ'
              '')

x = Person()
print(x.eyes)
x.eat()

lee = Student()
print(lee.eyes)
lee.study()