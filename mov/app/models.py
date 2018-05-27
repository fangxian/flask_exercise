from . import db
from datetime import datetime
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, index=True)  # 编号
    name = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    pwd = db.Column(db.String(100))
    info = db.Column(db.Text)  # 个人说明
    icon = db.Column(db.String(255), unique=True)  # 头像，应该不用定义唯一
    phone = db.Column(db.String(11), unique=True)
    add_time = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    uuid = db.Column(db.String(100), unique=True)
    #userlogs = db.relationship('UserLog', backref='user')  # 外键关联关系， 用user来反向检索到users表
    articles = db.relationship('Article', backref='user')
    #comments = db.relationship('Comment', backref='user')
    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)

'''
class UserLog(db.Model):
    pass


class Role(db.Model):
    pass
'''

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    url = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(255), unique=True)
    content = db.Column(db.Text)
    add_time = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    #comments = db.relationship("Comment", backref='article')

    def __repr__(self):
        return "<article %r>" % self.id


class Comment(db.Model):
    __tablename = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    #article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Comment %r" % self.id