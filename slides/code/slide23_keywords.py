
from slide12_walkthru import MetaWaterfowl

print("# Before class with __init_subclass__")

class Swan(metaclass=MetaWaterfowl):

    def __init_subclass__(subclass, **kw):
      print("consuming", kw)
      super().__init_subclass__(subclass)

print("# Between class with __init_subclass__ and subclass")

class BlackSwan(Swan, key="word"):
    pass

print(f"# End of module {__name__}")
