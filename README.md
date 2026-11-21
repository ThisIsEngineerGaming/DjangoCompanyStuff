# Slippery Company - "Company Information" web app (Django)

## Running

```
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Then open http://127.0.0.1:8000/

## Structure

- `company_site/` - project settings and root `urls.py` (includes the app's URLs).
- `sections/` - the app with everything about the site sections:
  - `data.py`  - sections, subsections and their content
  - `views.py` - class-based views (`SectionView` + one subclass per section)
  - `urls.py`  - routes for sections, subsections and catch-all
- `products/` - the second app: product catalog
  - `classes.py` - user-defined class `Product` and `summarize()`
  - `data.py`, `views.py`, `urls.py` - data, views (reuse `SectionView`), routes
  - `templatetags/shop_extras.py` - custom filter `money`
  - the views pass nested dicts with lists of `Product` objects to the templates
    (`products.html`, `product_list.html`, `_product_card.html`), which use
    `with`, `if/else`, `for`, filters `length`, `pluralize`, `join`, `title`,
    `truncatechars`, `add` and the custom `money`
- Template inheritance: `base.html` -> `products_base.html` -> `products.html`;
  child templates extend blocks `meta_description` and `footer_text` with
  `{{ block.super }}` and fill the `banner` block.
- `templates/`, `static/` - HTML templates, CSS and images.

## Routes

| Address                                   | Page                         |
|-------------------------------------------|------------------------------|
| `/`                                       | Home                         |
| `/news/`                                  | News (all)                   |
| `/news/company`, `/news/products`, `/news/events` | News subsections     |
| `/products/`                              | Products (all)               |
| `/products/women`, `/products/men`, `/products/kids`, `/products/accessories` | Product subsections |
| `/management/`                            | Management (all)             |
| `/management/board`, `/management/executives`, `/management/departments` | Management subsections |
| `/about/`                                 | About                        |
| `/about/history`, `/about/mission`, `/about/values` | About subsections  |
| `/contacts/`, `/contact/`                 | Contacts                     |
| `/contacts/france`, `/contacts/ukraine`, `/contacts/austria` | Offices by country |

Subsection addresses work with or without the trailing slash.
Any other path after a section's address (for example `/news/12345`,
`/about/our-story/1991`, `/contacts/odesa/office-sadova`) shows that
section's overview. Other unknown addresses show the 404 page (the custom
template `templates/404.html` is used when `DEBUG = False`).

To add a subsection, add an entry to `SECTIONS` in `sections/data.py`.
