import peewee
import config

db = peewee.MySQLDatabase(config.DATABASE["database"],
                          host=config.DATABASE["host"],
                          port=config.DATABASE["port"],
                          user=config.DATABASE["user"],
                          passwd=config.DATABASE["password"])
