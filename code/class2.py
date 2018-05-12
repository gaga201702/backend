class Foo():
    def __init__(self):
        self.id = 8
        self.value = self.get_value()

    def get_value(self):
        pass
    def should_destroy_earth(self):
        return self.id == 42
    
class Baz(Foo):
    def __init__(self):
        print("init foo")
    def get_value(self, some_new_parameter):
    """Since 'get_value' is called from the base class's
    __init__ method and the base class definition doesn't
    take a parameter, trying to create a Baz instance will
    fail.
    """
        print("A")
        pass
