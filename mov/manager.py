from flask_script import Manager
from app import app, db

manager = Manager(app)

if __name__ == '__main__':
    #db.create_all()
    manager.run()
    #app.run()