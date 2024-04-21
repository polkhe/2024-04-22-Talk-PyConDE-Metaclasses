class MetaWaterfowl(type):

    def __init__(cls, cls_name, bases, cls_dict, **kw):
        print(f'** __init__ in metaclass para', cls_name)
        super().__init__(cls_name, bases, cls_dict, **kw)

    def __repr__(cls):
        cls_name = cls.__name__
        return f"<Classe para fazer {cls_name!r}>"


class Waterfowl(metaclass=MetaWaterfowl):

    registro = {}

    def __init_subclass__(subclass):
        print(f'** registrando', subclass.__name__)
        subclass.registro[subclass.__name__] = subclass

    def __class_getitem__(cls, name):
        return cls.registro[name]


VALID_ANATIDAE = {
    'Duck',
    'Ganso',
    'Marreco',
    'Cisne',
}

def verifica_Waterfowl(cls):
    print("** verificando:", cls.__name__)
    name = cls.__name__
    if name not in VALID_ANATIDAE:
        raise RuntimeError(
            f"{name} is not quacky enough."
        )


@verifica_Waterfowl
class Duck(Waterfowl):

    def quack(self):
        print("Quack!")
