
#括号中的object表示继承的父类
class People(object):
    def say(self):
        print('I am a people')

class Student(object):
    ##class_name是类属性
    class_name = 'Student'
    # __init__ 是构造函数，第一个参数永远是self
    def __init__(self, name, score):
        ##name, score是实例属性。实例属性的优先级比类属性的优先级高
        self.name = name;
        ##属性名前面加下划线表示是私有的，默认不加为public
        self.__score = score;

    #自定义函数
    def print_score(self):
        print('%s : %s ' % (self.name, self.__score))

    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'

    #私有属性score最好通过get set 方法访问
    def get_score(self):
        return self.__score

    def set_score(self, sc):
        if 0<= sc <= 100:
            self.__score = sc
        else:
            return ValueError('bad score')

    def say(self):
        print('I am a student')


def say(pp):
    pp.say()


def set_name_outof_class(self, name):
    self.name = name

#相当于java中的main函数
if __name__ == "__main__":
    lisa = Student('Lisa', 95)
    lisa.print_score()
    grade = lisa.get_grade()
    print('%s \'s grade is %s' % (lisa.name, grade))

    #say方法中传的参数不要求是有继承关系的，只要People类中和Student类中都有say方法。Java中不允许。
    #鸭子类型。一个对象只要看起来像鸭子，叫起来像鸭子，就可以被看做是鸭子
    say(People())
    say(lisa)

    #列出参数的所有属性及方法
    dir(lisa)

    #python中可以动态的给类加上额外的方法。这在java中是不可能的。。
    Student.set_name = set_name_outof_class
    lisa.set_name('Bart')
    lisa.print_score()
