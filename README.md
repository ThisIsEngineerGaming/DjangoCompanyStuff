# Slippery Company — "Company Information" web app (Django)

## Running

```
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Then open http://127.0.0.1:8000/

## Routes

| Address                   | Section    |
|---------------------------|------------|
| `/`                       | Home       |
| `/news/`                  | News       |
| `/management/`            | Management |
| `/about/`                 | About      |
| `/contacts/`, `/contact/` | Contacts   |

Any path after a section's address (for example `/news/12345`,
`/about/our-story/1991`, `/contacts/odesa/office-sadova`) also shows that
section. Other unknown addresses show the 404 page (the custom template
`templates/404.html` is used when `DEBUG = False`).
