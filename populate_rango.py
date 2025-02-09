import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we create lists of dictionaries containing the pages
    # we want to add into each category.
    # Now we add views for each page.
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/', 'views': 10},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/', 'views': 5},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 7}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 15},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/', 'views': 12},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 9}
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/', 'views': 4},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org', 'views': 6}
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    # Iterate through the categories and add them to the database
    for cat, cat_data in cats.items():
        category = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(category, p['title'], p['url'], p['views'])

    # Print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    category, created = Category.objects.get_or_create(name=name, defaults={'views': views, 'likes': likes})
    if not created:
        print(f'Category "{name}" already exists. Using existing category.')
    return category

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
