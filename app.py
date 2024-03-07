from flask import Flask, url_for, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY']='my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

connect_db(app)
db.create_all()

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

@app.route('/')
def pet_list():
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data 
        age = form.age.data 
        notes = form.notes.data 
        available = form.available.data
        
        pet = Pet(name=name, species=species, photo=photo, age=age, notes=notes, available=available)
        
        db.session.add(pet)
        db.session.commit()
        
        return redirect('/') 
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/delete/<int:pet_id>', methods=['POST'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    
    db.session.delete(pet)
    db.session.commit()
    
    return redirect(url_for('pet_list'))


@app.route("/pets/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo = form.photo.data
        db.session.commit()
        return redirect(url_for('pet_list'))

    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)