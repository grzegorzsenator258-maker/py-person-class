class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for person in people:
        Person(person["name"], person["age"])
        person_list.append(Person.people[person["name"]])

    for person in people:
        if "wife" in person:
            if person["wife"] != None:
                Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] != None:
                Person.people[person["name"]].husband = Person.people[person["husband"]]
    return person_list
