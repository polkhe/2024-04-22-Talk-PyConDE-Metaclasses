
def pause(msg):
    input(f'{msg}. globals:\n{list(globals())}')


pause("*** Before CONSTANT")

CONSTANT = "value"

pause("*** Before the class")


class Duck:

    pause("*** Start of class declaration")

    def __init__(self):
        pause("*** Inside instance __init__")

    def quack(self):
        pause("Quak!")

    pause("*** End of class declaration")


pause("*** After the class")
