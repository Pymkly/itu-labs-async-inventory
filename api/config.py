import os
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

HOST = str(config.get("POSTGRESQL", "HOST"))
DATABASE = str(config.get("POSTGRESQL", "DATABASE"))
USER = str(config.get("POSTGRESQL", "USER"))
PASSWORD = str(config.get("POSTGRESQL", "PASSWORD"))

