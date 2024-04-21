class better_repr_type(type):

    def __init__(cls, name, bases, namespace_dict):

        # cls above is the class under construction

        def __repr__(self):
            attr_repr = ', '.join(
                f'{name}={value!r}'
                for name, value in self.__dict__.items()
            )
            cls = self.__class__
            return f'{cls.__name__}({attr_repr})'

        # Injecting instance method:
        cls.__repr__ = __repr__

        super().__init__(name, bases, namespace_dict)

    # Method for use by the class under construction itself
    def __repr__(cls):
        bases = ', '.join(c.__name__ for c in cls.__bases__)
        return f'{cls.__name__}({bases})'

    x = 25
