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
        assert isinstance(self.ser.list_attrs(), dict)
        assert self.ser.list_attrs().get("name") == "myclass"
