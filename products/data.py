"""
Content of the "Products" section (second app of the project).

Same structure as sections/data.py. Extra item fields:
    price - text shown on the card
    image - file name inside static/img/
"""

SECTIONS = {
    'products': {
        'title': 'Products',
        'subsections': {
            'women': {
                'title': 'Women',
                'intro': 'Soft, warm and stylish slippers for her.',
                'items': [
                    {'heading': 'Cloud Walker', 'price': '$29', 'image': 'slipper-purple.svg',
                     'text': 'Our bestseller: memory-foam insole and a non-slip sole.'},
                    {'heading': 'Winter Rink', 'price': '$35', 'image': 'slipper-orange.svg',
                     'text': 'Fleece-lined and extra warm for cold tiled floors.'},
                ],
            },
            'men': {
                'title': 'Men',
                'intro': 'Comfort-first house footwear for him.',
                'items': [
                    {'heading': 'Sofa Captain', 'price': '$32', 'image': 'slipper-dark.svg',
                     'text': 'A roomy fit with a firm sole for walks to the kitchen.'},
                    {'heading': 'Morning Coffee', 'price': '$27', 'image': 'slipper-purple.svg',
                     'text': 'Light, breathable and easy to slip on.'},
                ],
            },
            'kids': {
                'title': 'Kids',
                'intro': 'Little feet, big comfort.',
                'items': [
                    {'heading': 'Tiny Steps', 'price': '$19', 'image': 'slipper-orange.svg',
                     'text': 'Bright colours and a grippy sole for young explorers.'},
                    {'heading': 'Puddle Jumper', 'price': '$22', 'image': 'slipper-dark.svg',
                     'text': 'Washable and quick drying.'},
                ],
            },
            'accessories': {
                'title': 'Accessories',
                'intro': 'Everything to keep your slippers (and feet) happy.',
                'items': [
                    {'heading': 'Cosy Socks', 'price': '$9',
                     'text': 'Pair them with any slipper for extra warmth.'},
                    {'heading': 'Slipper Care Kit', 'price': '$12',
                     'text': 'Brush and gentle cleaner to keep soles and fabric fresh.'},
                ],
            },
        },
    },
}
