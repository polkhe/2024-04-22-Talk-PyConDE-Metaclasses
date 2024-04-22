
class MyClass:

    x = 42

    def double(self):
        return self.x * 2


class MyMixin:

    def increase(self):
        return self.x + 2


class MySubClass(MyClass, MyMixin):

    x = 36
