class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, value):
        self.age = value

    def set_name(self, value):
        self.name = value

    def __str__(self):
        return f"Animal: {self.name}, {self.age}"


class Dog(Animal):
    def speak(self):
        print("Woof")

    def __str__(self):
        return f"Caine: {self.name}, {self.age}"


class Person(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def get_friends(self):
        return self.friends

    def print_friends(self):
        for f in self.friends:
            print(f)
        print()

    def __str__(self):
        return f"Person: {self.name}, {self.age}"


if __name__ == '__main__':
    a = Animal("Pisica", 3)
    a.set_name("Caine")

    print(a)
    print(a.get_name(), a.get_age())

    azorel = Dog("Azorel", 7)
    print(azorel)
    azorel.speak()

    maria = Person("Maria", 20)
    andrei = Person("Andrei", 21)
    george = Person("George", 23)

    maria.add_friend(andrei)
    andrei.add_friend(maria)
    andrei.add_friend(george)
    george.add_friend(andrei)

    print(f"{maria.get_name()}'s friends:")
    maria.print_friends()
    print(f"{andrei.get_name()}'s friends:")
    andrei.print_friends()
    print(f"{george.get_name()}'s friends:")
    george.print_friends()
