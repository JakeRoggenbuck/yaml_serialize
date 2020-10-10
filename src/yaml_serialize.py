import yaml


class ObjectDict:
    """Generate dictionary representation of object arguments"""
    def __init__(self, _object: object):
        self._object = _object

    def get_attrs(self):
        return self._object.__dict__


class YamlDump:
    def __init__(self, object_dict: dict, outfile: str):
        self.object_dict = object_dict
        self.outfile = outfile

    def generate_yaml(self):
        """Generate yaml string from object_dict"""
        return yaml.dump(self.object_dict)

    def write_file(self):
        with open(self.outfile, "w") as file:
            return file.write(self.generate_yaml())


class Serialize:
    def __init__(self, object_to_serialize, name: str = False):
        self.object_to_serialize = object_to_serialize
        self.object_dict = ObjectDict(object_to_serialize)
        self.default_name = name
        self.name = self.generate_name()

    def generate_name(self):
        if self.default_name is False:
            return self.object_to_serialize.__class__.__name__
        else:
            return self.default_name
