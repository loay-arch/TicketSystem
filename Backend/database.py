import psycopg
from credentials import host,port,dbname,user,password
from datetime import datetime
import StatusAndRoles
def get_connection():
    try:
        con = psycopg.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        return con
    except Exception as e:
        print(e)
        return None


def add_Department(name):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO departments (department_name) VALUES (%s)", (name,))
        con.commit()
        return {"status": True,"message": "Successfully added department"}
    except psycopg.errors.UniqueViolation:
        return {"status": False,"message": "Department already exists"}
    except Exception as e:
        return {"status": False,"message": str(e)}
    finally:
        con.close()

def delete_Department(name):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM departments WHERE department_name=%s", (name,))
        if cur.rowcount == 0:
            return {"status": False, "message": "Department does not exist"}
        con.commit()
        return {"status": True,"message": "Successfully deleted department"}
    except Exception as e:
        return {"status": False,"message": str(e)}
    finally:
        con.close()

def update_Department(name, new_name):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE departments SET department_name=%s WHERE department_name=%s", (new_name, name))
        if cur.rowcount == 0:
            return {"status": False, "message": "Department does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully updated department"}
    except Exception as e:
        return {"status": False,"message": str(e)}
    finally:
        con.close()

def get_Departments():
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM departments")
        departments = cur.fetchall()
        return {"status": True, "departments": departments}
    except Exception as e:
        return {"status": False,"message": str(e)}
    finally:
        con.close()


def  add_Employee(name,id , department, role, password):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO employees (id, name, department_name, role, hashed_password) VALUES (%s, %s, %s, %s, %s)",(id, name, department, role, password))
        con.commit()
        return {"status": True, "message": "Successfully added employee"}
    except psycopg.errors.UniqueViolation:
        return {"status": False, "message": "Employee already exists"}
    except psycopg.errors.ForeignKeyViolation:
        return {"status": False, "message": "Employee department does not exist"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def delete_employee(id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM employees WHERE id=%s", (id,))
        if cur.rowcount == 0:
            return {"status": False, "message": "Employee does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully deleted employee"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()


def verify_employee(id,password):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM employees WHERE id=%s AND hashed_password=%s", (id,password,))
        employee = cur.fetchone()
        if employee is None:
            return {"status": False, "message": "Employee id or password incorrect"}
        return {"status": True, "role": employee[2]}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()


def get_Employees():
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
        return {"status": True, "employees": employees}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def add_Ticket(id, title, created_by, description):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO tickets (id, title, created_by, created_at, description, status) VALUES (%s, %s, %s, %s, %s, %s)",(id, title, created_by,datetime.now(), description, StatusAndRoles.Status.OPEN))
        con.commit()
        return {"status": True, "message": "Successfully added ticket"}
    except psycopg.errors.UniqueViolation:
        return {"status": False, "message": "Ticket ID already exists"}
    except psycopg.errors.ForeignKeyViolation:
        return {"status": False, "message": "Employee id doesnt exist"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def delete_ticket(id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM tickets WHERE id=%s", (id,))
        if cur.rowcount == 0:
            return {"status": False, "message": "Ticket does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully deleted ticket"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def get_Tickets():
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM tickets")
        tickets = cur.fetchall()
        return {"status": True, "tickets": tickets}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def get_ticket(id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM tickets WHERE id=%s", (id,))
        ticket = cur.fetchone()
        if ticket is None:
            return {"status": False, "message": "Ticket does not exist"}
        return {"status": True, "ticket": ticket}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def assign_ticket_to_employee(e_id,t_id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE tickets SET assigned_to=%s WHERE id=%s", (e_id, t_id))
        if cur.rowcount == 0:
            return {"status": False, "message": "Ticket id or Employee id does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully assigned ticket to employee"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def update_ticket_status(ticket_id, status):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE tickets SET status=%s WHERE id=%s", (status, ticket_id))
        if cur.rowcount == 0:
            return {"status": False, "message": "Ticket does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully updated ticket status"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def resolve_ticket(ticket_id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE tickets set status=%s, resolved_at = %s WHERE id=%s", (StatusAndRoles.Status.RESOLVED,datetime.now() ,ticket_id))
        if cur.rowcount == 0:
            return {"status": False, "message": "Ticket does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully resolved ticket"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def add_ticket_employee(id,status):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO ticket_assistant (employee_id, status) VALUES (%s, %s)",(id, status))
        con.commit()
        return {"status": True, "message": "Successfully added employee"}
    except psycopg.errors.UniqueViolation:
        return {"status": False, "message": "Employee already exists"}
    except psycopg.errors.ForeignKeyViolation:
        return {"status": False, "message": "Cannot find employee ID"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def delete_ticket_employee(id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM ticket_assistant WHERE employee_id=%s", (id,))
        if cur.rowcount == 0:
            return {"status": False, "message": "Employee does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully deleted employee"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def get_ticket_employees():
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM ticket_assistant")
        tickets = cur.fetchall()
        return {"status": True, "tickets": tickets}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()

def update_ticket_employee_status(id, status):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE ticket_assistant SET status=%s WHERE employee_id=%s", (status, id))
        if cur.rowcount == 0:
            return {"status": False, "message": "Employee does not exist"}
        con.commit()
        return {"status": True, "message": "Successfully updated employee status"}
    except Exception as e:
        return {"status": False, "message": str(e)}
    finally:
        con.close()
