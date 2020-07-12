import psycopg2
from site_integration import db
class Parrains(db.Model):
    __tablename__ = 'parrains'

    # id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(30), nullable=False)
    nom = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    formation = db.Column(db.String(10), nullable=False)
    tel = db.Column(db.Integer, primary_key=True,unique=True, nullable=False)
    image_file = db.Column(db.String(200), nullable=False, default='default.png')

    def __repr__(self):
        return f"User('{self.prenom}','{self.nom}', '{self.email}','{self.formation }', {self.tel}', {self.image_file}')"

class Filleuls(db.Model):
    __tablename__ = 'filleuls'

    # id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(30), nullable=False)
    nom = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    formation = db.Column(db.String(10), nullable=False)
    tel = db.Column(db.Integer, primary_key=True,unique=True, nullable=False)
    image_file = db.Column(db.String(200), nullable=False, default='default.png')
    tel_p = db.Column(db.Integer, nullable= True)

    def __repr__(self):
        return f"User('{self.prenom}','{self.nom}', '{self.email}','{self.formation }', {self.tel}', {self.image_file}')"