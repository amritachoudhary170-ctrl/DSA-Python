class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"My name is {self.name}")

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.isSitting = i

    def introduce_self(self):
        print(f"My name is {self.name}")
        
r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)

p1 = Person("Alice", "agressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()