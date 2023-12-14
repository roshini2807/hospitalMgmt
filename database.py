from peewee import *

db = SqliteDatabase('hospital.db')
db.connect()

class Doctor(Model):
    name = CharField()
    specialization = CharField()
    class Meta:
        database = db 

class Patient(Model):
    name = CharField()
    age = CharField()
    docID = ForeignKeyField(Doctor, backref='patients', null=True)
    class Meta:
        database = db 

def set_up_database():
    db.drop_tables([Doctor, Patient], safe=True)
    db.create_tables([Doctor, Patient])

def get_doctors(id=None):
    if id==None:
        doctors = Doctor.select()
    else:
        doctors = Doctor.select().where(Doctor.id == id)
    return doctors

def get_filtered_doctors(query):
    doctors = Doctor.select().where(Doctor.name.contains(query))
    return doctors

def add_doctor(name, specialization):
    doctor = Doctor(name=name, specialization=specialization)
    doctor.save()

def update_doctor(id, name, specialization):
    doctor = Doctor.select().where(Doctor.id == id).get()
    doctor.specialization = specialization
    doctor.name = name
    doctor.save()

def delete_doctor(id):
    doctor = Doctor.select().where(Doctor.id == id).get()
    doctor.delete_instance()

## Patient Entiity operations
def get_patients(id=None):
    if id==None:
        patients = Patient.select()
    else:
        patients = Patient.select().where(Patient.id == id)
    return patients

def get_filtered_patient(query):
    patients = Patient.select().where(Patient.name.contains(query))
    return patients

def add_patient(name, age, docID):
    patient = Patient(name=name, age=age)
    if(docID != 'none'):
        patient.docID = docID
    patient.save()

def update_patient(id, name, age, docID):
    patient = Patient.select().where(Patient.id == id).get()
    patient.name = name
    patient.age = age
    if(docID != 'none'):
        patient.docID = docID
    patient.save()

def delete_patient(id):
    patient = Patient.select().where(Patient.id == id).get()
    patient.delete_instance()