# SaitPD

Django web application for a student project - an informational site with pages for participants, a journal, resources and general info.

## Tech stack

- Python, **Django 4.2**
- HTML templates, static files
- SQLite (default)

## Pages

Home, About, Participants, Journal, Resources.

## Run

    pip install -r requirements.txt
    cp .env.example .env
    python manage.py migrate
    python manage.py runserver