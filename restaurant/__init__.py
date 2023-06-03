from flask import Flask
from collections import Counter


app = Flask(__name__)
'''app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)'''

table_no = Counter(range(1,21))
for i in table_no:
    table_no[i]=0

'''
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"'''

from . import routes
