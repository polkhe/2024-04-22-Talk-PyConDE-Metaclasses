print('* Start of module {__name__}')

from collections import UserDict

class LogDict(UserDict):
    def __setitem__(self, key, item):
        print("*** new attribute", key)
        return super().__setitem__(key, item)


class MetaWaterfowl(type):
    print('** Start of metaclass')

    @classmethod
    def __prepare__(metacls, cls_name, cls_bases, **kw):
        print("*** preparing class namespace")

        def debug(msg):
            print("** in class:", cls_name, "message:", msg)

        cls_dict = LogDict({'debug': debug})
        return cls_dict

    def __new__(meta_cls, cls_name, bases, cls_dict, **kw):
        print('*** __new__ in metaclass')

        cls_dict = dict(cls_dict)
        del cls_dict['debug']
        cls = super().__new__(meta_cls, cls_name, bases, cls_dict, **kw)

        return cls

    def __init__(cls, cls_name, bases, cls_dict, **kw):
        print('*** __init__ in metaclass')
        super().__init__(cls_name, bases, cls_dict, **kw)

    def __call__(cls):
        print('*** __call__ in metaclass')
        return super().__call__()

    def __repr__(cls):
        cls_name = cls.__name__
        return "<Class {cls_name!r} with MetaWaterfowl repr>"

    print('** End of metaclass')


print('* Between metaclass and class')


class Duck(metaclass=MetaWaterfowl):

    debug("Start of class declaration")

    def __new__(cls):
        print("*** Inside __new__ of Duck")
        return super().__new__(cls)

    def __init__(self):
        print("*** Inside __init__ of Duck")

    def quack(self):
        print("Quack!")

    debug("End of class declaration")


print('* Between class and subclass')


class MandarinDuck(Duck):

    debug("Start of subclass declaration")

    def quack(self):
        print("Quak!")

    debug("End of subclass declaration")


print('* Between subclass and instance creation')

duck = Duck()

print(f'* End of module {__name__}')
