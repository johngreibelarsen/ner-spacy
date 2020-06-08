import random
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('I am <<PERSON>> I need some help', {'entities': [(5, 15, 'PERSON')]})
DATA_TEMPLATE_1 = ('<<PERSON>> here, I have a question', {'entities': [(0, 10, 'PERSON')]})
DATA_TEMPLATE_2 = ('My name is <<PERSON>>', {'entities': [(11, 21, 'PERSON')]})
DATA_TEMPLATE_3 = ('Hi Bot I am <<PERSON>>', {'entities': [(12, 22, 'PERSON')]})
DATA_TEMPLATE_4 = ('Hi Barclays my name is <<PERSON>>', {'entities': [(23, 33, 'PERSON')]})
DATA_TEMPLATE_5 = ('My account name is <<PERSON>>', {'entities': [(19, 29, 'PERSON')]})
DATA_TEMPLATE_6 = ('Call me <<PERSON>>', {'entities': [(8, 18, 'PERSON')]})
DATA_TEMPLATE_7 = ('Regards <<PERSON>>', {'entities': [(8, 18, 'PERSON')]})
DATA_TEMPLATE_8 = ('Best wishes <<PERSON>>', {'entities': [(12, 22, 'PERSON')]})
DATA_TEMPLATE_9 = ('All the best <<PERSON>>', {'entities': [(13, 23, 'PERSON')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(person, template):
    str = template[0]
    str = str.replace('<<PERSON>>', person)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 10 + len(person), 'PERSON') # -10 length of <<PERSON>> string
    return (str, {'entities': [indexes]})


def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        name = fake.name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        names = [name, first_name, last_name]
        chosen_name = names[random.randint(0, 2)]
        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(chosen_name, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(50)
    print(entries)








