import os
name = os.environ.get('AIRBNB_ENV')

if (name == "development"):
    dev = True
else:
    dev = False

DEBUG = True if dev else False
HOST = 'localhost' if dev else '0.0.0.0'
PORT = 3333 if dev else 3000
DATABASE = {'host' : 'webone.johnserrano.tech',
            'user' : 'airbnb_user_dev' if dev else 'airbnb_user_prod',
            'database' : 'airbnb_dev' if dev else 'airbnb_prod',
            'port' : 21 if dev else 3306,
            'charset' : 'utf8',
            'password' : os.environ.get('AIRBNB_DATABASE_PWD_DEV') if dev else os.environ.get('AIRBNB_DATABASE_PWD_PROD')}
