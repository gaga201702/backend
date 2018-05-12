class Foo():
    def __init__(self):
        self.id = 8
        self.value = self.get_value()

    def get_value(self):
        pass
    def should_destroy_earth(self):
        return self.id == 42
class Baz(Foo):
    def get_value(self, some_new_parameter):
        """Since 'get_value' is called from the base class's
        __init__ method and the base class definition doesn't
        take a parameter, trying to create a Baz instance will
        fail.
        """
        pass
class Qux(Foo):
    """We aren't aware of Foo's internals, and we innocently
    create an instance attribute named 'id' and set it to 42.
    This overwrites Foo's id attribute and we inadvertently
    blow up the earth.
    """
    def __init__(self):
        super(Qux, self).__init__()
        self.id = 42
# No relation to Foo's id, purely coincidental
q = Qux()
b = Baz() # Raises 'TypeError'
q.should_destroy_earth() # returns True
q.id == 42 # returns True
