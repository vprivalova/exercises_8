import json
import functools
import xml.etree.ElementTree as ET
import yaml


def to_format(format='json'):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args):
            resulting = func(*args)
            if format == 'json':
                return json.dumps(resulting, indent=3)

            elif format == 'xml':
                root = ET.Element(resulting[0])
                info = ET.SubElement(root, 'info')
                data = ' '.join(resulting[1])
                info.text = data
                xml_str = ET.tostring(root, encoding="utf-8")
                return xml_str

            elif format == 'yaml':
                return yaml.dump(resulting)

        return wrapped
    return decorator


@to_format()
def text_structure(*args):
    structure = []
    paragraphs = 1
    for elem in args:
        structure.append((f'para {paragraphs}', elem))
        paragraphs += 1
    return structure


@to_format('xml')
def candidate(name='user', age='undefined', gender='undefined', university='nsu'):
    clients = ["clients", [name, age, gender, university]]
    return clients


@to_format('yaml')
def school_library(*args):
    library = {}
    for elem in args:
        library[elem[0]] = elem[1]
    return library


print(text_structure('Italian food is very tasty. It presents a wide range of dishes and drinks.',
                     'Pizza', 'This dish consists of a round-shaped dough and a filling.'))

print(candidate('Viktoria', '19', 'woman'))

print(school_library(('english language', 28), ('russian language', 76), ('algebra', 52), ('geography', 14)))
