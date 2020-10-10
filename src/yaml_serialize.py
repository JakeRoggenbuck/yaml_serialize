class Serialize:
    def __init__(self, object):
        self.object = object

    def get_attrs(self):
        return self.object.__dict__


class YamlDump:
    def __init__(self, serialize_object):
        self.serialize_object = serialize_object
