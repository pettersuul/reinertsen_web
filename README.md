# reinertsen_web

Requirements:
  - Python 3
  - Sass (Optional)
  - Heroku (Optional)

## 1. Setup

'pip install -r requirements.txt'

Store local settings in local_settings.py

```python
SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = False

# Contentful
SPACE_ID = ''
ACCESS_TOKEN = ''
ENVIRONMENT = ''
```

## 2. Run

'heroku local' or 'python manage.py runserver'

## 3. Develop

'sass --watch'
