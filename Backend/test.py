from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import StatusAndRoles
import hashlib
import database
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def log_in(user_id, password):
    h = hashlib.sha256()
    h.update(password.encode("utf-8"))
    return database.verify_employee(user_id, h.hexdigest())


@app.post("/departments")
def add_Department(department_name):
    return database.add_Department(department_name)

@app.put("/departments/{department_name}")
def update_department(department_name, new_department_name):
    return database.update_Department(department_name, new_department_name)

@app.delete("/departments/{department_name}")
def delete_department(department_name):
    return database.delete_Department(department_name)

@app.get("/departments")
def get_departments():
    return database.get_Departments()

@app.post("/employees")
def add_Employee(name, id, department, role, password):
    h = hashlib.sha256()
    h.update(password.encode("utf-8"))
    return database.add_Employee(name, id, department, role, h.hexdigest())

@app.delete("/employees/{id}")
def delete_employee(id):
    return database.delete_employee(id)

@app.get("/employees")
def get_employees():
    return database.get_Employees()
@app.post("/tickets")
def add_Ticket(id, title, created_by,description):
    return database.add_Ticket(id, title, created_by,description)

@app.delete("/tickets/{id}")
def delete_ticket(id):
    return database.delete_ticket(id)

@app.get("/tickets")
def get_tickets():
    return database.get_Tickets()

@app.post("/tickets/{ticket_id}/assign")
def assign_ticket_to_employee(employee_id, ticket_id):
    result = database.assign_ticket_to_employee(employee_id, ticket_id)
    if result["status"] == False:
        return result
    result = database.update_ticket_status(ticket_id,StatusAndRoles.Status.IN_PROGRESS)
    if result["status"] == False:
        return result
    result = database.update_ticket_employee_status(employee_id,StatusAndRoles.Status.UNAVAILABLE)
    if result["status"] == False:
        return result
    return {"status": True, "message": "Ticket assigned to employee successfully"}

@app.post("/tickets/{ticket_id}")
def resolve_ticket(ticket_id):
    result = database.resolve_ticket(ticket_id)
    if result["status"] == False:
        return result
    result = database.get_ticket(ticket_id)
    if result["status"] == False:
        return result
    ticket = result["ticket"]
    emp_id = ticket[7]
    result = database.update_ticket_employee_status(emp_id,StatusAndRoles.Status.AVALIABLE)
    if result["status"] == False:
        return result
    return {"status": True, "message": "Ticket resolved successfully"}




