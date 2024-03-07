
from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://as2.ftcdn.net/v2/jpg/04/93/18/11/1000_F_493181171_SctymCwX0Uu3v5lKNtRiZ90ByrjSQqIk.jpg"

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True) 
    
    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo or GENERIC_IMAGE
    
def connect_db(app):
    db.app = app
    db.init_app(app)
