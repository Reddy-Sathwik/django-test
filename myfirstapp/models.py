# myapp/models.py

from mongoengine import Document, StringField, IntField, DateField

class Person(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    dob = DateField(required=True)
