"""
Content of the site: sections and their subsections.

Every subsection is available at /<section>/<slug>/ (with or without the
trailing slash), e.g. /contacts/france, /news/events, /about/history.

Item fields (all optional except `heading`):
    heading - card title
    date    - datetime.date (news)
    role    - job title (management)
    text    - paragraph of text
    lines   - list of short lines (address, phone, email ...)
"""
from datetime import date

SECTIONS = {
    # ------------------------------------------------------------------ news
    'news': {
        'title': 'News',
        'subsections': {
            'company': {
                'title': 'Company',
                'intro': 'What is happening inside Slippery Company.',
                'items': [
                    {
                        'heading': 'New office opens in Odesa',
                        'date': date(2026, 10, 28),
                        'text': 'The Slippery Company team is now working in Tairove too. '
                                'Partners are welcome to drop by for coffee and a slipper test drive.',
                    },
                    {
                        'heading': 'Paris showroom is open',
                        'date': date(2026, 11, 3),
                        'text': 'Our first French showroom welcomes visitors every day '
                                'except Sunday.',
                    },
                ],
            },
            'products': {
                'title': 'Products',
                'intro': 'New collections and awards for our slippers.',
                'items': [
                    {
                        'heading': 'Introducing the "Winter Rink" collection',
                        'date': date(2026, 11, 12),
                        'text': 'A line of warm house slippers with a non-slip sole, '
                                'perfect for slippery tiled floors.',
                    },
                    {
                        'heading': 'Award for "Most Comfortable Footwear of the Year"',
                        'date': date(2026, 9, 5),
                        'text': 'An independent jury recognized the "Cloud Walker" model '
                                'for its softness, design and durability.',
                    },
                ],
            },
            'events': {
                'title': 'Events',
                'intro': 'Where you can meet the Joes in person.',
                'items': [
                    {
                        'heading': 'Autumn Slipper Expo in Kyiv',
                        'date': date(2026, 10, 15),
                        'text': 'Three days of demos, workshops and free foot massages.',
                    },
                    {
                        'heading': 'Vienna Comfort Summit',
                        'date': date(2026, 11, 20),
                        'text': 'Joe 3 will talk about the future of house footwear.',
                    },
                ],
            },
        },
    },

    # ------------------------------------------------------------ management
    'management': {
        'title': 'Management',
        'subsections': {
            'board': {
                'title': 'Board of Directors',
                'intro': 'The people who decide where the company walks next.',
                'items': [
                    {
                        'heading': 'Joe 1',
                        'role': 'Chief Executive Officer (CEO)',
                        'text': 'Leads the company and believes comfort starts with the feet.',
                    },
                    {
                        'heading': 'Joe 2',
                        'role': 'Chief Technology Officer (CTO)',
                        'text': 'In charge of materials, production and quality control.',
                    },
                ],
            },
            'executives': {
                'title': 'Executive Team',
                'intro': 'The Joes who run the company day to day.',
                'items': [
                    {
                        'heading': 'Joe 3',
                        'role': 'Chief Marketing Officer (CMO)',
                        'text': 'Tells the brand story and looks after our community of customers.',
                    },
                    {
                        'heading': 'Joe 4',
                        'role': 'Chief Financial Officer (CFO)',
                        'text': "Keeps the balance between the company's ambitions and the numbers.",
                    },
                    {
                        'heading': 'Joe 5',
                        'role': 'Chief Operating Officer (COO)',
                        'text': 'Makes sure every pair of slippers gets where it needs to go.',
                    },
                ],
            },
        },
    },

    # ----------------------------------------------------------------- about
    'about': {
        'title': 'About',
        'subsections': {
            'history': {
                'title': 'History',
                'intro': 'From a tiny workshop to offices in three countries.',
                'items': [
                    {'heading': '2010',
                     'text': 'Slippery Company is founded by a small team dreaming of the perfect house slipper.'},
                    {'heading': '2015',
                     'text': 'We open our first office in Kyiv and launch the "Cloud Walker" line.'},
                    {'heading': '2026',
                     'text': 'Offices in Ukraine, France and Austria, and a growing family of Joes.'},
                ],
            },
            'mission': {
                'title': 'Mission',
                'intro': 'Why we get up in the morning (in comfortable slippers).',
                'items': [
                    {'heading': 'Everyday comfort for everyone',
                     'text': 'From the first step in the morning to the last one in the evening.'},
                ],
            },
            'values': {
                'title': 'Values',
                'intro': 'What we stand on.',
                'items': [
                    {'heading': 'Comfort without compromise'},
                    {'heading': 'High-quality, eco-friendly materials'},
                    {'heading': 'Honesty with customers and partners'},
                    {'heading': "Safety in every step - a sole that doesn't slip!"},
                ],
            },
        },
    },

    # -------------------------------------------------------------- contacts
    'contacts': {
        'title': 'Contacts',
        'subsections': {
            'france': {
                'title': 'France',
                'intro': 'Our French offices and showrooms.',
                'items': [
                    {'heading': 'Paris',
                     'lines': ['12 Rue de la Paix', '+33 1 00 00 00 01', 'paris@slippery.example']},
                    {'heading': 'Lyon',
                     'lines': ['5 Place Bellecour', '+33 4 00 00 00 02', 'lyon@slippery.example']},
                ],
            },
            'ukraine': {
                'title': 'Ukraine',
                'intro': 'Where it all started.',
                'items': [
                    {'heading': 'Kyiv',
                     'lines': ['10 Khreshchatyk St., Office 5', '+38 (044) 000-00-01', 'kyiv@slippery.example']},
                    {'heading': 'Odesa',
                     'lines': ['7 Sadova St. (Tairove)', '+38 (048) 000-00-02', 'odesa@slippery.example']},
                ],
            },
            'austria': {
                'title': 'Austria',
                'intro': 'Our Austrian offices.',
                'items': [
                    {'heading': 'Vienna',
                     'lines': ['8 Mariahilfer Strasse', '+43 1 000 0001', 'vienna@slippery.example']},
                    {'heading': 'Graz',
                     'lines': ['3 Herrengasse', '+43 316 000002', 'graz@slippery.example']},
                ],
            },
        },
    },
}
