from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError
from site_integration.models import Filleuls, Parrains

class InscriptionForm(FlaskForm):
   
    prenom = StringField('Prénom(s)',
                            validators=[DataRequired(), Length(min=2, max=30)])
    nom = StringField('Nom',
                            validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])

    formation = SelectField('Formation',choices=[('dsti1','DSTI1'),('dsti2','DSTI2'),('dsttr1','DSTTR1'),('dsttr2','DSTTR2')],validators=[DataRequired()])
    tel = StringField('Téléphone', validators=[DataRequired(), Length(min=9,max=12), Regexp('\d{9,12}')])
    image_file = FileField('Photo',validators=[FileAllowed(['jpg','png', 'jpeg'])])
    submit = SubmitField('Soumettre')

    def validate_email(self, email):
        email1 = Filleuls.query.filter_by(email=email.data).first()
        email2 = Parrains.query.filter_by(email=email.data).first()
        if email1 or email2:
            raise ValidationError("That email is taken.Please choose a different email.")
    
    def validate_tel(self, tel):
        tel1 = Filleuls.query.filter_by(tel=tel.data).first()
        tel2 = Parrains.query.filter_by(email=tel.data).first()
        if tel1 or tel2:
            raise ValidationError('This number is taken.Please choose a different number.')


