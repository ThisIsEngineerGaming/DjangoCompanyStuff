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
- `products/` - the second app: product catalog (`data.py`, `views.py`, `urls.py`);
  it reuses `SectionView` from `sections` with its own data.
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
