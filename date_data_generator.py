import random
import datetime
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('Todays date is <<DATE>>', {'entities': [(15, 23, 'DATE')]})
DATA_TEMPLATE_1 = ('On this date: <<DATE>>', {'entities': [(14, 22, 'DATE')]})
DATA_TEMPLATE_2 = ('You sent me this email on <<DATE>>', {'entities': [(26, 34, 'DATE')]})
DATA_TEMPLATE_3 = ('I made a complaint on <<DATE>> about my bill', {'entities': [(22, 30, 'DATE')]})
DATA_TEMPLATE_4 = ('You called me on <<DATE>> so I am returning the call ', {'entities': [(17, 25, 'DATE')]})
DATA_TEMPLATE_5 = ('I was contacted early yesterday <<DATE>>, ', {'entities': [(32, 40, 'DATE')]})
DATA_TEMPLATE_6 = ('Date <<DATE>>', {'entities': [(5, 13, 'DATE')]})
DATA_TEMPLATE_7 = ('I received you notification last week <<DATE>>', {'entities': [(38, 46, 'DATE')]})
DATA_TEMPLATE_8 = ('I am available on <<DATE>> to discuss further', {'entities': [(18, 26, 'DATE')]})
DATA_TEMPLATE_9 = ('I do not understand my bill from <<DATE>>', {'entities': [(33, 41, 'DATE')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(date, template):
    str = template[0]
    str = str.replace('<<DATE>>', date)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 8 + len(date), 'DATE') # -8 length of <<DATE>> string
    return (str, {'entities': [indexes]})


def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        patterns0 = ['%d-%m-%Y', '%d-%m-%y', '%d/%m/%Y', '%d/%m/%y']
        patterns1 = ['%d%m%Y', '%d%m%y', '%d-%m-%Y', '%d-%m-%y', '%d/%m/%Y', '%d/%m/%y', '%d %m %Y', '%d %m %y', '%b%d%Y', '%b%d%y', '%b-%d-%Y', '%b-%d-%y', '%b/%d/%Y', '%b/%d/%y', '%b %d %Y', '%b %d %y']
        patterns2 = ['%m%d%Y', '%m%d%y', '%m-%d-%Y', '%m-%d-%y', '%m/%d/%Y', '%m/%d/%y', '%m %d %Y', '%m %d %y']

        if i % 4 == 0:
            patterns = patterns1
        elif i % 15 == 0:
            patterns = patterns2
        else:
            patterns = patterns0

        chosen_pattern = patterns[random.randint(0, len(patterns) - 1)]
        date = fake.date(chosen_pattern)
        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(date, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(50)
    print(entries)







