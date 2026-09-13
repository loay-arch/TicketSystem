import psycopg
from credentials import host,port,dbname,user,password
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
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def delete_Department(name):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM departments WHERE department_name=%s", (name,))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def update_Department(name, new_name):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE departments SET department_name=%s WHERE department_name=%s", (new_name, name))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def  add_Employee(name,id , department, role):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO employees (id, name, department_name, role) VALUES (%s, %s, %s, %s)",(id, name, department, role))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def delete_employee(id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM employees WHERE id=%s", (id,))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def add_Ticket(id, title, created_by, created_at, description, status):
    con = get_connection()

    if con is None:
        return False

    try:
        cur = con.cursor()

        cur.execute("INSERT INTO tickets (id, title, created_by, created_at, description, status) VALUES (%s, %s, %s, %s, %s, %s)",(id, title, created_by, created_at, description, status))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False

    finally:
        con.close()

def delete_ticket(id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM tickets WHERE id=%s", (id,))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def assign_ticket_to_employee(t_id,e_id):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE tickets SET assigned_to=%s WHERE id=%s", (e_id, t_id))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

def update_ticket_status(ticket_id, status):
    con = get_connection()
    if con is None:
        return False
    try:
        cur = con.cursor()
        cur.execute("UPDATE tickets SET status=%s WHERE id=%s", (status, ticket_id))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        con.close()

