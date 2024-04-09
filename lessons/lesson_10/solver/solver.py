# Модуль сложения для которого хотим написать тесты
class Solver:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b





# if __name__ == '__main__':
#     a = Solver(3, 8)
#     print(a.add())