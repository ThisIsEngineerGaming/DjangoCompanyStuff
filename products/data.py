"""
Content of the "Products" section (second app of the project).

Same structure as sections/data.py, but every subsection's `items`
is a list of `Product` objects (see classes.py).
"""
from .classes import Product

SECTIONS = {
    'products': {
        'title': 'Products',
        'subsections': {
            'women': {
                'title': 'Women',
                'intro': 'Soft, warm and stylish slippers for her.',
                'items': [
                    Product('Cloud Walker', 29, 'Our bestseller: memory-foam insole and a non-slip sole.',
                            'slipper-purple.svg', tags=['bestseller', 'memory foam']),
                    Product('Winter Rink', 28, 'Fleece-lined and extra warm for cold tiled floors.',
                            'slipper-orange.svg', old_price=35, tags=['warm', 'winter']),
                    Product('Rose Petal', 31, 'Light satin slippers for summer evenings.',
                            'slipper-purple.svg', in_stock=False, tags=['light']),
                ],
            },
            'men': {
                'title': 'Men',
                'intro': 'Comfort-first house footwear for him.',
                'items': [
                    Product('Sofa Captain', 32, 'A roomy fit with a firm sole for walks to the kitchen.',
                            'slipper-dark.svg', tags=['roomy']),
                    Product('Morning Coffee', 27, 'Light, breathable and easy to slip on.',
                            'slipper-purple.svg', tags=['light', 'breathable']),
                    Product('Night Owl', 36, 'Quiet soles that will not wake up the neighbours.',
                            'slipper-dark.svg', old_price=45, tags=['quiet']),
                ],
            },
            'kids': {
                'title': 'Kids',
                'intro': 'Little feet, big comfort.',
                'items': [
                    Product('Tiny Steps', 19, 'Bright colours and a grippy sole for young explorers.',
                            'slipper-orange.svg', tags=['grippy']),
                    Product('Puddle Jumper', 22, 'Washable and quick drying.',
                            'slipper-dark.svg', tags=['washable']),
                ],
            },
            'accessories': {
                'title': 'Accessories',
                'intro': 'Everything to keep your slippers (and feet) happy.',
                'items': [
                    Product('Cosy Socks', 9, 'Pair them with any slipper for extra warmth.', tags=['warm']),
                    Product('Slipper Care Kit', 12, 'Brush and gentle cleaner to keep soles and fabric fresh.',
                            in_stock=False, tags=['care']),
                ],
            },
        },
    },
}
