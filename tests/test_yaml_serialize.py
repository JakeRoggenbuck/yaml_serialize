import yaml_serialize


class MyClass:
    def __init__(self):
        self.name = "myclass"


class TestSerialize:
    def setup_method(self):
        self.ser = yaml_serialize.Serialize(MyClass)

    def test_serialize_exist(self):
        yaml_serialize.Serialize(MyClass)

    def test_serialize_attrs(self):
        assert hasattr(self.ser, "object")
