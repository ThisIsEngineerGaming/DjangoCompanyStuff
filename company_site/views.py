from django.shortcuts import render

NEWS = [
    {
        'date': 'November 12, 2026',
        'title': 'Introducing the new "Winter Rink" collection',
        'text': 'We have launched a line of warm house slippers with a '
                'non-slip sole, perfect for slippery tiled floors.',
    },
    {
        'date': 'October 28, 2026',
        'title': 'New office opens in Odesa',
        'text': 'The Slippery Company team is now working in Tairove too. '
                'Partners are welcome to drop by for coffee and a slipper test drive.',
    },
    {
        'date': 'September 5, 2026',
        'title': 'Award for "Most Comfortable Footwear of the Year"',
        'text': 'An independent jury recognized the "Cloud Walker" model '
                'for its softness, design and durability.',
    },
]

MANAGEMENT = [
    {
        'name': 'Joe 1',
        'role': 'Chief Executive Officer (CEO)',
        'bio': 'Leads the company and believes comfort starts with the feet.',
    },
    {
        'name': 'Joe 2',
        'role': 'Chief Technology Officer (CTO)',
        'bio': 'In charge of materials, production and quality control.',
    },
    {
        'name': 'Joe 3',
        'role': 'Chief Marketing Officer (CMO)',
        'bio': 'Tells the brand story and looks after our community of customers.',
    },
    {
        'name': 'Joe 4',
        'role': 'Chief Financial Officer (CFO)',
        'bio': 'Keeps the balance between the company\'s ambitions and the numbers.',
    },
    {
        'name': 'Joe 5',
        'role': 'Chief Operating Officer (COO)',
        'bio': 'Makes sure every pair of slippers gets where it needs to go.',
    },
]

OFFICES = [
    {
        'city': 'Kyiv',
        'address': '10 Khreshchatyk St., Office 5',
        'phone': '+38 (044) 000-00-01',
        'email': 'kyiv@slippery.example',
    },
    {
        'city': 'Odesa',
        'address': '7 Sadova St. (Tairove)',
        'phone': '+38 (048) 000-00-02',
        'email': 'odesa@slippery.example',
    },
]


# The `_` parameter is needed for the catch-all routes (<path:_>): Django
# passes the rest of the path into it. We don't use it, but must accept it.

def home(request, _=None):
    return render(request, 'home.html', {'section': 'home'})


def news(request, _=None):
    return render(request, 'news.html', {'section': 'news', 'news': NEWS})


def management(request, _=None):
    return render(request, 'management.html',
                  {'section': 'management', 'managers': MANAGEMENT})


def about(request, _=None):
    return render(request, 'about.html', {'section': 'about'})


def contacts(request, _=None):
    return render(request, 'contacts.html',
                  {'section': 'contacts', 'offices': OFFICES})


def page_not_found(request, exception=None):
    return render(request, '404.html', {'section': None}, status=404)
