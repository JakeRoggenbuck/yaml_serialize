import os
import yaml_serialize


class MyClass:
    def __init__(self):
        self.name = "myclass"


class TestObjectDict:
    def setup_method(self):
        myclass = MyClass()
        self.object_dict = yaml_serialize.ObjectDict(myclass)

    def test_object_dict_exist(self):
        myclass = MyClass()
        yaml_serialize.ObjectDict(myclass)

    def test_object_dict_attrs(self):
        assert hasattr(self.object_dict, "_object")

    def test_get_attrs(self):
        assert isinstance(self.object_dict.get_attrs(), dict)
        assert self.object_dict.get_attrs().get("name") == "myclass"


class TestYamlDump:
    def setup_method(self):
        myclass = MyClass()
        object_dict = yaml_serialize.ObjectDict(myclass).get_attrs()
        self.yaml_dump = yaml_serialize.YamlDump(object_dict)

    def test_yaml_dump_attrs(self):
        assert hasattr(self.yaml_dump, "object_dict")

    def test_generate_yaml(self):
        yaml = self.yaml_dump.generate_yaml()
        assert isinstance(yaml, str)
        assert "name" in yaml
        assert "myclass" in yaml

    def test_write_file(self):
        write = self.yaml_dump.write_file("TEST_file")
        assert isinstance(write, int)
        os.remove("TEST_file")


class TestSerialize:
    def setup_method(self):
        self.myclass = MyClass()

    def test_generate_name(self):
        ser = yaml_serialize.Serialize(self.myclass)
        assert ser.generate_name() == "MyClass"

        ser = yaml_serialize.Serialize(self.myclass)
        assert ser.generate_name("MyName") == "MyName"

    def test_wtite(self):
        ser = yaml_serialize.Serialize(self.myclass)
        assert isinstance(ser.write(), int)
        os.remove("MyClass")

        ser = yaml_serialize.Serialize(self.myclass)
        assert isinstance(ser.write("MyName"), int)
        os.remove("MyName")

    def test_get(self):
        ser = yaml_serialize.Serialize(self.myclass)
        yaml = ser.get()
        assert isinstance(yaml, str)
