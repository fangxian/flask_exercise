from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@127.0.0.1/movie"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "movie app"
app.config["REDIS_URL"] = "redis://192.168.4.1:6379/0"
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)


from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint

app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(home_blueprint)



