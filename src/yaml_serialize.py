class Serialize:
    def __init__(self, object):
        self.object = object

    def list_attrs(self):
        return self.object.__dict__
