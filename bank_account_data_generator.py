import random
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('What does a bank account number look like, something like this <<UK_BANK_NUMBER>>', {'entities': [(63, 81, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_1 = ('My bank account number is <<UK_BANK_NUMBER>>', {'entities': [(26, 44, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_2 = ('Can I please request you help with my account no. <<UK_BANK_NUMBER>>', {'entities': [(50, 68, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_3 = ('Can you help me with my account <<UK_BANK_NUMBER>>, please call me', {'entities': [(32, 50, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_4 = ('Bank Account <<UK_BANK_NUMBER>>', {'entities': [(13, 31, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_5 = ('Help, I forgot my account no. I think it was <<UK_BANK_NUMBER>>, where can I see it, ', {'entities': [(45, 63, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_6 = ('Account No: <<UK_BANK_NUMBER>>', {'entities': [(12, 30, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_7 = ('I need help with my account, number is <<UK_BANK_NUMBER>>', {'entities': [(39, 57, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_8 = ('I need to speak to someone about my account <<UK_BANK_NUMBER>>, can you give me a phone number or email', {'entities': [(44, 62, 'UK_BANK_NUMBER')]})
DATA_TEMPLATE_9 = ('Dear bot, I need your to tell me about my bank account: <<UK_BANK_NUMBER>>', {'entities': [(56, 74, 'UK_BANK_NUMBER')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(account_no, template):
    str = template[0]
    str = str.replace('<<UK_BANK_NUMBER>>', account_no)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 18 + len(account_no), 'UK_BANK_NUMBER') # -18 length of <<UK_BANK_NUMBER>> string
    return (str, {'entities': [indexes]})


def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        account_no = str(random.randint(10000000, 99999999))
        if i % 25 == 0:
            account_no = '0' + str(random.randint(1000000, 9999999))
        separators = [' ', ' ', '', '', '', '', '', '', '', '', '', '', '', '', '-']
        chosen_separator = separators[random.randint(0, 14)]
        separator_space = random.randint(0, 9)
        if separator_space < 2:
            account_no = account_no[0:2] + chosen_separator + account_no[2:4] + chosen_separator + account_no[4:6] + chosen_separator + account_no[6:8]
        else:
            account_no = account_no[0:4] + chosen_separator + account_no[4:8]

        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(account_no, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(25)
    print(entries)







