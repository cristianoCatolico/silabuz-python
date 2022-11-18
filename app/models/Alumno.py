from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Alumno(db.Model):
    id = db.Column(db.Integer, autoincrement = True ,primary_key = True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(10), nullable=False)
    dni= db.Column(db.String(8),nullable=True, unique=True)
    fecha_nac= db.Column(db.DateTime, default=datetime.utcnow)
    idAula = db.Column(db.Integer, db.ForeignKey('salon.id'), primary_key = True)
