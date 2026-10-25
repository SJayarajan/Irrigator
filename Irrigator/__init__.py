from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'santhosh@45229_loves_python'
from Irrigator import routes