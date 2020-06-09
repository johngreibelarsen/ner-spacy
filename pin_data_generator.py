import random
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('What does a PIN look like, I think my is <<PIN_NUMBER>>', {'entities': [(41, 55, 'PIN_NUMBER')]})
DATA_TEMPLATE_1 = ('My pin number is <<PIN_NUMBER>>', {'entities': [(17, 31, 'PIN_NUMBER')]})
DATA_TEMPLATE_2 = ('I urgent need help with my pin no. <<PIN_NUMBER>>', {'entities': [(35, 49, 'PIN_NUMBER')]})
DATA_TEMPLATE_3 = ('Can you please help me with my PIN <<PIN_NUMBER>>, please call me', {'entities': [(35, 49, 'PIN_NUMBER')]})
DATA_TEMPLATE_4 = ('PIN Number <<PIN_NUMBER>>', {'entities': [(11, 25, 'PIN_NUMBER')]})
DATA_TEMPLATE_5 = ('Help, I forgot my PIN. I think it is <<PIN_NUMBER>>, can I see it somewhere, ', {'entities': [(37, 51, 'PIN_NUMBER')]})
DATA_TEMPLATE_6 = ('Forgot my pin: <<PIN_NUMBER>>', {'entities': [(15, 29, 'PIN_NUMBER')]})
DATA_TEMPLATE_7 = ('Lost my card can I block my PIN <<PIN_NUMBER>>', {'entities': [(32, 46, 'PIN_NUMBER')]})
DATA_TEMPLATE_8 = ('I need to talk to an agent about my PIN <<PIN_NUMBER>>, can you give transfer me', {'entities': [(40, 54, 'PIN_NUMBER')]})
DATA_TEMPLATE_9 = ('Hello, I have received my pin by mail, shown here <<PIN_NUMBER>> but have received no card', {'entities': [(50, 64, 'PIN_NUMBER')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(pin_no, template):
    str = template[0]
    str = str.replace('<<PIN_NUMBER>>', pin_no)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 14 + len(pin_no), 'PIN_NUMBER') # -14 length of <<PIN_NUMBER>> string
    return (str, {'entities': [indexes]})


def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        pin_no = str(random.randint(1000, 9999))
        if i % 12 == 0:
            pin_no = '0' + str(random.randint(100, 999))
        if i % 20 == 0:
            pin_no = str(random.randint(10000, 99999))

        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(pin_no, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(25)
    print(entries)







