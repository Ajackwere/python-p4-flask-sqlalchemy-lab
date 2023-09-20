from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import Date
from datetime import date


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default='None')
    birthday = db.Column(Date, nullable=False, default='None')
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(100), nullable=False, default='None')
    open_to_visitors = db.Column(db.Boolean, default=True)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False)

