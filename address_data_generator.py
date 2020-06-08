import random
from faker import Faker
fake = Faker(['en_GB'])

DATA_TEMPLATE_0 = ('I live at <<LOC>>', {'entities': [(10, 17, 'LOC')]})
DATA_TEMPLATE_1 = ('My address is <<LOC>>', {'entities': [(14, 21, 'LOC')]})
DATA_TEMPLATE_2 = ('Can I please request you help with my address <<LOC>>', {'entities': [(46, 53, 'LOC')]})
DATA_TEMPLATE_3 = ('Can you please send to <<LOC>>', {'entities': [(23, 30, 'LOC')]})
DATA_TEMPLATE_4 = ('You can find me here <<LOC>>', {'entities': [(21, 28, 'LOC')]})
DATA_TEMPLATE_5 = ('My location is <<LOC>>', {'entities': [(15, 22, 'LOC')]})
DATA_TEMPLATE_6 = ('Send it here please <<LOC>> and I will return asap', {'entities': [(20, 27, 'LOC')]})
DATA_TEMPLATE_7 = ('Address: <<LOC>>', {'entities': [(9, 16, 'LOC')]})
DATA_TEMPLATE_8 = ('How can I change my address details. My contact details are <<LOC>>', {'entities': [(60, 67, 'LOC')]})
DATA_TEMPLATE_9 = ('Have moved to this new location <<LOC>> before I lived at some other address in town', {'entities': [(32, 39, 'LOC')]})

DATA_TEMPLATES = [DATA_TEMPLATE_0, DATA_TEMPLATE_1, DATA_TEMPLATE_2, DATA_TEMPLATE_3, DATA_TEMPLATE_4, DATA_TEMPLATE_5,
                  DATA_TEMPLATE_6, DATA_TEMPLATE_7, DATA_TEMPLATE_8, DATA_TEMPLATE_9]


def create_entry(address, template):
    str = template[0]
    str = str.replace('<<LOC>>', address)
    start_index = template[1]['entities'][0][0]
    end_index = template[1]['entities'][0][1]
    indexes = (start_index, end_index - 7 + len(address), 'LOC') # -7 length of <<LOC>> string
    return (str, {'entities': [indexes]})

cities = ['Bath', 'Ely', 'Birmingham', 'St Neots', 'Manchester', 'Southampton', 'Bradford', 'Nottingham', 'Bristol', 'Cambridge', 'Coventry',
          'Leeds', 'Liverpool', 'London', 'Oxford', 'Leicester', 'Peterborough', 'Portsmouth', 'Sunderland', 'Westminster', 'Wolverhampton', 'York']

def create_entries(no_of_entries):
    entries = []
    for i in range(no_of_entries):
        address = fake.address().replace("\n", " ")
        postcode = fake.postcode().replace("\n", " ")
        short_address_1 = (fake.street_address() + ' ' + postcode).replace("\n", " ")
        short_address_2 = (postcode + ', ' + fake.street_address()).replace("\n", " ")
        short_address_3 = (fake.street_address() + ' ' + fake.city() + ' ' + postcode).replace("\n", " ")
        short_address_4 = (fake.street_address() + ' ' + cities[random.randint(0, len(cities) - 1)] + ' ' + postcode).replace("\n", " ")
        addresses = [address, postcode, short_address_1, short_address_2, short_address_3, short_address_4, address, address]
        chosen_address = addresses[random.randint(0, 7)]
        chosen_template = DATA_TEMPLATES[random.randint(0, len(DATA_TEMPLATES) - 1)]
        entry = create_entry(chosen_address, chosen_template)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    entries = create_entries(50)
    print(entries)







