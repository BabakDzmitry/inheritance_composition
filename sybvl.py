# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-super/


class A:
    def __init__(self):
        print("Initializing: class A")

    def sub_method(self, b):
        print("sub_method from class A:", b)


class B(A):
    def __init__(self):
        print("Initializing: class B")
        super().__init__()

    def sub_method(self, b):
        print("sub_method from class B:", b)
        super().sub_method(b + 1)


class X(B):
    def __init__(self):
        print("Initializing: class X")
        super().__init__()

    def sub_method(self, b):
        print("sub_method from class X:", b)
        super().sub_method(b + 1)


class Y(X):
    def __init__(self):
        print("Initializing: class Y")
        # super() с параметрами
        super(X, self).__init__()

    def sub_method(self, b):
        print("sub_method from class Y:", b)
        super().sub_method(b + 1)


x = X()
x.sub_method(1)
print("Обратите внимание как происходит инициализация")
print("классов при указании аргументов в функции super()")
y = Y()
y.sub_method(5)
