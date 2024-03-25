import json


def to_json(func):
    def wrapped(*args):
        resulting = func(*args)
        return json.dumps(resulting, indent=3)
    return wrapped


@to_json
def text_structure(*args):
    structure = []
    paragraphs = 1
    for elem in args:
        structure.append((f'para {paragraphs}', elem))
        paragraphs += 1
    return structure


@to_json
def personal_id(name='user', age='undefined', gender='undefined', university='nsu'):
    candidate = {"name": name, "age": age, "gender": gender, "university": university}
    return candidate


print(text_structure('Italian food is very tasty. It presents a wide range of dishes and drinks.',
                     'Pizza', 'This dish consists of a round-shaped dough and a filling.'))
print(personal_id('Viktoria', 19, 'woman'))
