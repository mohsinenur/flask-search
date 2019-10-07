from flask import Flask
import os
from search.main.controllers import main
from search.database import db
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(main, url_prefix='/')
# app.register_blueprint(admin, url_prefix='/admin')