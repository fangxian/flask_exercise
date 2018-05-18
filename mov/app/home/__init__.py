from flask import blueprints

home = blueprints("home", __name__)
import app.home.views
