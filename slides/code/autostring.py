class AutoStringDict(dict):

    def __missing__(self, key: str):
        if key.startswith('__') and key.endswith('__'):
            # skip special atributes/methods
            raise KeyError(key)

        # creates key and value on demand
        self[key] = key.capitalize()
        return key


class AutoStringMeta(type):
    def __prepare__(name, bases, **kwargs):
        return AutoStringDict()


class AutoString(metaclass=AutoStringMeta):
    pass
