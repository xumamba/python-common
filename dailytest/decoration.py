

class Student(object):
    _score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


if __name__ == '__main__':
    stu = Student()
    print(stu.score)
    stu.score = 99
    print(stu.score)
