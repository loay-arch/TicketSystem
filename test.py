from fastapi import FastAPI
import database
app = FastAPI()
@app.get("/")
def root():
    return {"Hello": "World"}
@app.post("/departments")
def add_Department(department_name):
    return database.add_Department(department_name)

@app.put("/departments/{department_name}")
def update_department(department_name, new_department_name):
    return database.update_Department(department_name, new_department_name)

@app.delete("/departments/{department_name}")
def delete_department(department_name):
    return database.delete_Department(department_name)

@app.post("/employees")
def add_Employee(name,id , department, role):
    return database.add_Employee(name, id, department, role)

@app.delete("/employees/{id}")
def delete_employee(id):
    return database.delete_employee(id)

@app.post("/tickets")
def add_Ticket(id, title, created_by, created_at, description, status):
    return database.add_Ticket(id, title, created_by, created_at, description, status)

@app.delete("/tickets/{id}")
def delete_ticket(id):
    return database.delete_ticket(id)

