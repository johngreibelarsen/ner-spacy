import random
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('What is a sort code like <<UK_SORT_CODE>>', {'entities': [(25, 41, 'UK_SORT_CODE')]})
DATA_TEMPLATE_1 = ('My sort is <<UK_SORT_CODE>>', {'entities': [(11, 27, 'UK_SORT_CODE')]})
DATA_TEMPLATE_2 = ('Can I please request you help with my address <<UK_SORT_CODE>>', {'entities': [(46, 62, 'UK_SORT_CODE')]})
DATA_TEMPLATE_3 = ('Can you help me with my sort code <<UK_SORT_CODE>>, please contact me', {'entities': [(34, 50, 'UK_SORT_CODE')]})
DATA_TEMPLATE_4 = ('Sort code <<UK_SORT_CODE>>', {'entities': [(10, 26, 'UK_SORT_CODE')]})
DATA_TEMPLATE_5 = ('Help, my sort code is <<UK_SORT_CODE>> lost, ', {'entities': [(22, 38, 'UK_SORT_CODE')]})
DATA_TEMPLATE_6 = ('Sort: <<UK_SORT_CODE>>', {'entities': [(6, 22, 'UK_SORT_CODE')]})
DATA_TEMPLATE_7 = ('I need help with my account, sort code <<UK_SORT_CODE>>', {'entities': [(39, 55, 'UK_SORT_CODE')]})
DATA_TEMPLATE_8 = ('I have a question about my sort code <<UK_SORT_CODE>>, you can see my account info', {'entities': [(37, 53, 'UK_SORT_CODE')]})
DATA_TEMPLATE_9 = ('Lovely speaking to you bot, I need your guidance on sort code issue. My code is <<UK_SORT_CODE>>', {'entities': [(80, 96, 'UK_SORT_CODE')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(sort_code, template):
    str = template[0]
    str = str.replace('<<UK_SORT_CODE>>', sort_code)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 16 + len(sort_code), 'UK_SORT_CODE') # -16 length of <<UK_SORT_CODE>> string
    return (str, {'entities': [indexes]})


def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        sort_code = str(random.randint(100000, 999999))
        if i % 25 == 0:
            sort_code = '0' + str(random.randint(10000, 99999))
        separators = [' ', ' ', ' ', '', '', '', '', '', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ':', '*']
        chosen_separator = separators[random.randint(0, 20)]
        sort_code = sort_code[0:2] + chosen_separator + sort_code[2:4] + chosen_separator + sort_code[4:6]
        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(sort_code, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(50)
    print(entries)







