# yaml-serialize

## Use
```py
from src import yaml_serialize


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

# Write serialized object with class name "MyObject.yml"
serializer.write()

# Write serialized object with custom name "MyCoolObject.yml"
serializer.write("MyCoolObject.yml")
```

## Output
```yml
!!python/object:src.yaml_serialize.ObjectDict
_object: !!python/object:__main__.MyObject
  age: 16
  favorite_color: Green
  mylist:
  - hey
  - this
  - is
  - cool
  name: Jake
```