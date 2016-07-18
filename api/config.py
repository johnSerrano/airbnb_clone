#defaults to production

import os
name = os.environ.get('AIRBNB_ENV')

DEBUG = False
HOST = '0.0.0.0'
PORT = 3000
DATABASE = {'host' : 'webone.johnserrano.tech',
            'user' : 'airbnb_user_prod',
            'database' : 'airbnb_prod',
            'port' : 3306,
            'charset' : 'utf8',
            'password' : os.environ.get('AIRBNB_DATABASE_PWD_PROD'),
            }

if name == "development":
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = {'host' : 'webone.johnserrano.tech',
                'user' : 'airbnb_user_dev',
                'database': 'airbnb_dev',
                'port' : 21,
                'charset' : 'utf8',
                'password' : os.environ.get('AIRBNB_DATABASE_PWD_DEV'),
                }

elif name == "test":
    DEBUG = True
    HOST = 'localhost'
    PORT = 5555
    DATABASE = {'host' : 'webone.johnserrano.tech',
                'user' : 'airbnb_user_test',
                'database' : 'airbnb_test',
                'port' : 21,
                'charset' : 'utf8',
                'password' : os.environ.get('AIRBNB_DATABASE_PWD_TEST'),
                }
