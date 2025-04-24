class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"
    
    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"
    
    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

g1 = Geeks('Alice')
g2 = Geeks('Bob')

print(Geeks.get_course())
print(Geeks.get_instance_count())

print(Geeks.welcome_message())