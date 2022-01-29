class Score():
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self, value):
        self.__mid = value

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, value):
        self.__final = value


score = Score(50, 75)
print((score.mid + score.final) / 2)