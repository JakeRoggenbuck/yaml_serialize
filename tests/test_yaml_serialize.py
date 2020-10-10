import yaml_serialize


class MyClass:
    def __init__(self):
        self.name = "myclass"


class TestSerialize:
    def setup_method(self):
        myclass = MyClass()
        self.ser = yaml_serialize.Serialize(myclass)

    def test_serialize_exist(self):
        myclass = MyClass()
        yaml_serialize.Serialize(myclass)

    def test_serialize_attrs(self):
        assert hasattr(self.ser, "object")

    def test_get_attrs(self):
        assert isinstance(self.ser.get_attrs(), dict)
        assert self.ser.get_attrs().get("name") == "myclass"


class TestYamlDump:
    def setup_method(self):
        myclass = MyClass()
        serialize_object = yaml_serialize.Serialize(myclass).get_attrs()
        self.yaml_dump = yaml_serialize.YamlDump(serialize_object)

    def test_yaml_dump_attrs(self):
        assert hasattr(self.yaml_dump, "serialize_object")
