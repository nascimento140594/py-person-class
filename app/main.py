from typing import Any, Dict, List, Optional


class Person:
    ## Class attribute to store instances by name
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        ## Optional relations initialized to None
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None

        ## Register this instance in the class-level dictionary
        Person.people[name] = self


def create_person_list(people_list: List[Dict[str, Any]]) -> List[Person]:
    """
    Convert a list of dicts to a list of Person instances.
    """
    ## First pass: create all Person instances and register them
    instances: List[Person] = []
    for person_dict in people_list:
        person = Person(person_dict["name"], person_dict["age"])
        instances.append(person)

    ## Second pass: set up wife/husband references
    for person_dict, person_obj in zip(people_list, instances):
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]

    return instances
