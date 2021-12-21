import os

# DB_ENDPOINT = os.environ['db_endpoint']
# DB_USER_NAME = os.environ['db_user_name']
# DB_SECRET_KEY = os.environ['db_password']
# DATABASE_NAME = os.environ['db_name']

DB_ENDPOINT = 'localhost'
DB_USER_NAME = 'root'
DB_SECRET_KEY = '123456'
DATABASE_NAME = 'medium_db'

DB_CONNECTION_STR="mysql+pymysql://"+DB_USER_NAME+":"+DB_SECRET_KEY+"@"+DB_ENDPOINT+"/"+DATABASE_NAME

API_PREFIX = '/api'
