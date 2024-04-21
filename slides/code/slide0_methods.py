
class MyClass:

    x = 42

    def dobrar(self):
        return self.x * 2


class MySubClass(MyClass):

    x = 36

    def __repr__(self):
        return f'<MySubClass x={self.x}>'

