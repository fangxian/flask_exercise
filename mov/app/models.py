from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) #编号
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(20))
    info = db.Column(db.Text) #个人说明
    icon = db.Column(db.String(255), unique=True) #头像，应该不用定义唯一
    phone = db.Column(db.String(11), unique=True)
    add_time = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    uuid = db.Column(db.String(100), unique=True)
    userlogs = db.relationship('UserLog', backref='user') #外键关联关系， 用user来反向检索到users表
    articles = db.relationship('Article', backref='user')
    comments = db.relationship('Comment', backref='user')
	
	def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)

		
class UserLog(db.Model):
    pass


class Role(db.Model):
    pass


class Article(db.Model):
    pass


class Comment(db.Model):
    pass
