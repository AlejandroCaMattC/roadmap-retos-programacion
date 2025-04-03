import os
import xml.etree.ElementTree as xml
import json

"""JSON and XML in Python"""

data = {
    "name": "Alejandro Campos",
    "age": 39,
    "birth_date": "17-06-1985",
    "programming_languages": ["Python", "JavaScript", "C++"]
}

# XML

xml_file = "alejodata.xml"


def create_xml():
    # Create the root element
    root = xml.Element("person")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print("XML file created successfully!")


create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())


os.remove(xml_file)
print("XML file deleted successfully!")


# JSON

json_file = "alejodata.json"


def create_jason():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data, indent=4)
        print("JSON file created successfully!")


create_jason()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)

"""Exercise"""

create_xml()
create_jason()


class Data:

    def __init__(self, name: str, age: int, birth_date: str, programming_languages: list[str]) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages


with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = int(root.find("age").text)
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.findall("programming_languages/item"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)


with open(json_file, "r") as json_data:
    json_dict = json.loads(json_data.read())
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["programming_languages"]
    )
    print(json_class.__dict__)
