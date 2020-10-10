import yaml


class Serialize:
    def __init__(self, object):
        self.object = object

    def get_attrs(self):
        return self.object.__dict__


class YamlDump:
    def __init__(self, serialize_object, outfile):
        self.serialize_object = serialize_object

    def generate_yaml(self):
        return yaml.dump(self.serialize_object)
