import yaml


class Serialize:
    def __init__(self, object):
        self.object = object

    def get_attrs(self):
        return self.object.__dict__


class YamlDump:
    def __init__(self, serialize_object, outfile):
        self.serialize_object = serialize_object
        self.outfile = outfile

    def generate_yaml(self):
        return yaml.dump(self.serialize_object)

    def write_file(self):
        with open(self.outfile, "w") as file:
            return file.write(self.generate_yaml())
