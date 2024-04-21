print("*** Before CONSTANT", list(globals()), sep='\n')

CONSTANT = "value"

print("*** Before the class", list(globals()), sep='\n')


class Duck:

    print("*** Start of class declaration", list(globals()), sep='\n')

    def __init__(self):
        print("*** Inside instance __init__", list(globals()), sep='\n')

    def quack(self):
        print("Quak!")

    print("*** End of class declaration", list(globals()), sep='\n')


print("*** After the class", list(globals()), sep='\n')
