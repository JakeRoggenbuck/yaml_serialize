from yaml_serialize import yaml_serialize


class MyObject:
    def __init__(self):
        self.name = "Jake"
        self.age = 16
        self.favorite_color = "Green"
        self.mylist = ["hey", "this", "is", "cool"]


my_object = MyObject()
serializer = yaml_serialize.Serialize(my_object)

# Get serialized object as string
my_serialized_object = serializer.get()
print(my_serialized_object)

# Write serialized object with class name "MyObject.yml"
serializer.write()

# Write serialized object with custom name "MyCoolObject.yml"
serializer.write("MyCoolObject.yml")

des = yaml_serialize.Deserialize()
new = des.read(my_serialized_object)
print(new)
