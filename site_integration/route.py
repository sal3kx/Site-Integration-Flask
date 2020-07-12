from flask import render_template, url_for, flash, redirect, request
from site_integration import app, db
from site_integration.forms import InscriptionForm
from site_integration.models import Filleuls, Parrains
import cloudinary.uploader
from random import random
from PIL import Image
import secrets
import os

def save_and_upload_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profil',picture_fn)

    output_size = (600, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    cloudinary.config(cloud_name='dyxx9ymns', api_key='628969687138542', api_secret='u29oBh20RLoiLhg77vITai61AvU')
    cloudinary.uploader.upload(picture_path, public_id = random_hex)
    return picture_fn

@app.route("/", methods=['GET', 'POST'])
def inscription():
    form = InscriptionForm()
    i = str(int(random()*5) + 1)
    bg = r'background/background4.png' if i == '4' else r'background/background'+ i +'.jpg'
    if form.validate_on_submit():
        picture_file = 'default.png'
        if form.image_file.data:
            picture_file = save_and_upload_picture(form.image_file.data)
            
        if form.formation.data == 'dsti1' or form.formation.data == 'dsttr1':
            user1 = Filleuls(prenom=form.prenom.data, nom=form.nom.data, email=form.email.data, formation=form.formation.data, tel=form.tel.data,
                     image_file=picture_file)

        if form.formation.data == 'dsti2' or form.formation.data == 'dsttr2':
            user1 = Parrains(prenom=form.prenom.data, nom=form.nom.data, email=form.email.data, formation=form.formation.data, tel=form.tel.data,
                     image_file=picture_file)
        db.session.add(user1)
        db.session.commit()
        flash('Inscription validé!','success')
        return redirect(url_for('inscription'))
    return render_template('inscription.html',titlte='Inscription', form=form, bg=bg)


@app.route("/parrainage")
def parrainage():
    return render_template('parrainage.html')