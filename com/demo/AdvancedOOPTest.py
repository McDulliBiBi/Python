
class Student(object):
    #__slots__是一个特殊的变量，用来限制该class实例能添加的属性
    __slots__ = ('name', 'score', '_birth')

    #property装饰器，被装饰的方法可以当做属性使用。简化代码
    @property
    def birth(self):
        return self._birth

    #birth属性是可读可写的，且在set方法中可以校验传的值是否正常
    @birth.setter
    def birth(self, v):
        if 1919 < v < 2019:
            self._birth = v
        else:
            return ValueError('bad birth')

    #age属性没有set方法，表示只读
    @property
    def age(self):
        return 2019 - self.birth  #这里其实调用的是birth get方法

    def print_info(self):
        print('name: %s, score: %s, birth: %s, age: %s' % (self.name, self.score, self.birth, self.age))

if __name__ =='__main__':
    s = Student()
    s.name = 'Lisa'
    s.score = 90
    s.birth = 1985 #这里其实调用的是birth set方法
    #s._birth = 1985  # 这样写没有调用birth set方法，直接给属性赋值了
    s.print_info()