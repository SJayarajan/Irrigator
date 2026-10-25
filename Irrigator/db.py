import os
from tinydb import TinyDB, Query

DB_PATH = os.path.join(os.path.dirname(__file__), 'irrigator_db.json')
db = TinyDB(DB_PATH)
users = db.table('users')
User = Query()