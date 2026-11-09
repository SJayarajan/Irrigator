from flask import Flask
from flask_wtf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'santhosh@45229_loves_python'
CSRFProtect(app)
from Irrigator import routes