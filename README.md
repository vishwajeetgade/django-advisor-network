## an advisor network where users can come and book an advisor for a call.
 Project includes authentication api which stores jwt token in cookies

## Technology stack
### Python 3.9
### Django rest framework
### MySQL

### git clone https://github.com/vishwajeetgade/django-advisor-network.git

## dependencies 
```
pip install
```
### django
### djangorestframework
### django-dotenv
### mysqlclient
### PyJWT==1.7.1


## How to run 
create file manage.py in folder django-advisor-network and paste the below code
```
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv


def main():
    """Run administrative tasks."""
    dotenv.read_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nurturelabsassignment.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

First create a MySQL database and connect to your database in .nurturelabsassignment.settings.py
## Run Following commands

```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```