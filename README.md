## an advisor network where users can come and book an advisor for a call.
 Project includes authentication api which stores jwt token in cookies

## Technology stack
### Python 3.9
### Django rest framework
### MySQL

### git clone https://github.com/vishwajeetgade/django-advisor-network.git

## dependencies 
```
pip install django==3.2.8
pip install djangorestframework==3.12.4
pip install django-dotenv==1.4.2
pip install corsheaders==3.10
pip install mysqlclient==2.0.3
pip install PyJWT==1.7.1
```


## How to run 

First create a MySQL database and connect to your database in .nurturelabsassignment.settings.py
## Run Following commands

```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```