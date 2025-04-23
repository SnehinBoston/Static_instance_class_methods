from class_static_instance import DemoClass
obj = DemoClass()
print(obj.instance_method())
print(obj.class_method())
print(obj.static_method())
print(DemoClass.class_method())
print(DemoClass.static_method())
# print(DemoClass.instance_method()) throws an error
obj = DemoClass()
print(DemoClass.instance_method(obj))
