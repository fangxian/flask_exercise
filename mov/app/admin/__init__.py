from flask import blueprints

admin = blueprints("admin", __name__)
import app.admin.views
