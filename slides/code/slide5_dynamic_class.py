
class MyClass:

    x = 42

    def double(self):
        return self.x * 2


class MyMixin:

    def increase(self):
        return self.x + 2


class MySubClass(MyClass, MyMixin):

    x = 36


def my_subclass_builder(new_x):

    class MyDynamicSubClass(MyClass, MyMixin):

        x = new_x

    return MyDynamicSubClass
