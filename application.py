from bottle import route, post, run, template, redirect, request
import database

database.set_up_database()

@route("/")
def get_patients():
    patients = database.get_patients()
    return template("list_patient.tpl", patients=patients)

@route("/add")
def get_add_patient():
    doctors = database.get_doctors()
    return template("add_patient.tpl", doctors=doctors)

@post("/add")
def post_add_patient():
    name = request.forms.get("name")
    age = request.forms.get("age")
    docID = request.forms.get("docID")
    database.add_patient(name, age, docID)
    redirect("/")    

@route("/update/<id>")
def get_update_patient(id):
    patient = database.get_patients(id)[0]
    doctors = database.get_doctors()
    docID = patient.docID.id if patient.docID else ''
    return template("update_patient.tpl", patient=patient, doctors=doctors, docID=docID)

@post("/update")
def post_update_patient():
    name = request.forms.get("name")
    age = request.forms.get("age")
    id = request.forms.get("id")
    docID = request.forms.get("docID")
    database.update_patient(id, name, age, docID)
    redirect("/")    

@route("/delete/<id>")
def get_delete_patient(id):
    database.delete_patient(id)
    redirect("/")


## Doctor routes
@route("/doctor")
def get_doctors():
    query = request.query.get("query")
    if(query):
        doctors = database.get_filtered_doctors(query)
    else:
        doctors = database.get_doctors()
        query = ''
    return template("list_doctor.tpl", doctors=doctors,query=query)

@route("/doctor/add")
def get_add_doctor():
    return template("add_doctor.tpl")

@post("/doctor/add")
def post_add_doctor():
    name = request.forms.get("name")
    specialization = request.forms.get("specialization")
    database.add_doctor(name, specialization)
    redirect("/doctor")    

@route("/doctor/update/<id>")
def get_update_doctor(id):
    doctors = database.get_doctors(id)
    return template("update_doctor.tpl", doctor=doctors[0])

@post("/doctor/update")
def post_update_doctor():
    name = request.forms.get("name")
    specialization = request.forms.get("specialization")
    id = request.forms.get("id")
    database.update_doctor(id, name, specialization)
    redirect("/doctor")    

@route("/doctor/delete/<id>")
def get_delete_doctor(id):
    database.delete_doctor(id)
    redirect("/doctor")


run(host='localhost', port=8080)