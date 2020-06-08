import random
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('Is a credit card always 16 digits, ex. shown <<CREDIT_CARD>>', {'entities': [(45, 60, 'CREDIT_CARD')]})
DATA_TEMPLATE_1 = ('My card number is <<CREDIT_CARD>>', {'entities': [(18, 33, 'CREDIT_CARD')]})
DATA_TEMPLATE_2 = ('Can I please have help with my card <<CREDIT_CARD>>', {'entities': [(36, 51, 'CREDIT_CARD')]})
DATA_TEMPLATE_3 = ('I have added my debit card details here: <<CREDIT_CARD>>, please check', {'entities': [(41, 56, 'CREDIT_CARD')]})
DATA_TEMPLATE_4 = ('Card details <<CREDIT_CARD>>', {'entities': [(13, 28, 'CREDIT_CARD')]})
DATA_TEMPLATE_5 = ('Help, I forgot my pin for my debit card: <<CREDIT_CARD>>, where can I find it, ', {'entities': [(41, 56, 'CREDIT_CARD')]})
DATA_TEMPLATE_6 = ('Credit or Debit Card: <<CREDIT_CARD>>', {'entities': [(22, 37, 'CREDIT_CARD')]})
DATA_TEMPLATE_7 = ('I need help with my card, the number is <<CREDIT_CARD>>', {'entities': [(40, 55, 'CREDIT_CARD')]})
DATA_TEMPLATE_8 = ('Can I please speak to someone that knows about cards <<CREDIT_CARD>>, you can reach me on phone or email anytime', {'entities': [(53, 68, 'CREDIT_CARD')]})
DATA_TEMPLATE_9 = ('Dear bot, how do I report my card stolen or lost, card is <<CREDIT_CARD>>', {'entities': [(58, 73, 'CREDIT_CARD')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(credit_card_no, template):
    str = template[0]
    str = str.replace('<<CREDIT_CARD>>', credit_card_no)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 15 + len(credit_card_no), 'CREDIT_CARD') # -15 length of <<CREDIT_CARD>> string
    return (str, {'entities': [indexes]})


def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        type_of_card = random.randint(0, 9)
        separators = [' ', ' ', ' ', ' ', '', '', '-']
        chosen_separator = separators[random.randint(0, 6)]
        if type_of_card < 8: # XXXX-XXXX-XXXX-XXXX
            credit_card_no = str(random.randint(1000000000000000, 9999999999999999))
            credit_card_no = credit_card_no[0:4] + chosen_separator + credit_card_no[4:8] + chosen_separator + credit_card_no[8:12] + chosen_separator + credit_card_no[12:16]
        elif type_of_card == 8: # AMEX 15 digits XXXX-XXXXXX-XXXXX
            credit_card_no = str(random.randint(100000000000000, 999999999999999))
            credit_card_no = credit_card_no[0:4] + chosen_separator + credit_card_no[4:10] + chosen_separator + credit_card_no[10:15]
        elif type_of_card == 9: # small card numbers XXXX-XXXX-XXXXX
            credit_card_no = str(random.randint(1000000000000, 9999999999999))
            credit_card_no = credit_card_no[0:4] + chosen_separator + credit_card_no[4:8] + chosen_separator + credit_card_no[8:13]

        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(credit_card_no, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(25)
    print(entries)







