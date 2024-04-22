from collections.abc import Mapping


class MetaWaterfowl(type):

    def __init__(cls, cls_name, bases, cls_dict, **kw):
        print('** __init__ in metaclass for', cls_name)
        super().__init__(cls_name, bases, cls_dict, **kw)

    def __repr__(cls):
        cls_name = cls.__name__
        return f"<Class for making {cls_name!r}>"


class Waterfowl(metaclass=MetaWaterfowl):

    registry: Mapping[str, type] = {}

    def __init_subclass__(subclass):
        print('** registering', subclass.__name__)
        subclass.registry[subclass.__name__] = subclass

    def __class_getitem__(cls, name):
        return cls.registry[name]


VALID_ANATIDAE = {
    'Duck',
    'Goose',
    'Drake',
    'Swan',
}

def check_waterfowl(cls):
    print("** verifying:", cls.__name__)
    name = cls.__name__
    if name not in VALID_ANATIDAE:
        raise RuntimeError(
            f"What a quack! {name} is not quacky enough."
        )
    print('** verified:', cls.__name__)
    return cls


@check_waterfowl
class Duck(Waterfowl):

    def quack(self):
        print("Quack!")
