
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class PetForm(FlaskForm):
    name=StringField("Name", validators=[InputRequired()])
    species=SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo=StringField("Photo URL",validators=[Optional(), URL()])
    age=FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes=TextAreaField("Notes/Description", validators=[Optional(), Length(min=10)])
    available=BooleanField("Available?")

class EditPetForm(FlaskForm):
   
    photo = StringField( "Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments",validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
