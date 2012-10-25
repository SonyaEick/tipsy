"""
model.py
"""
import sqlite3
import datetime

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):          
    c = db.cursor()                                     
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    c.execute(query, (email, password, name))           
    db.commit()

def remove_user(db, user_id):          
    c = db.cursor()                                     
    query = """DELETE FROM Users WHERE id =?"""                                                           
    c.execute(query, (user_id,) )           
    db.commit()
    return "Deleted User: %d" %user_id 

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

    return None

def new_task(db, title, user_id):
    """Given a title and a user_id, create a new task belonging to 
    that user. Return the id of the created task"""
    time_stamp= str(datetime.datetime.now())
    clean_time = time_stamp[:16]
    c= db.cursor()
    query = """INSERT INTO Tasks VALUES (NULL, ?, NULL, ?, ?) """
    c.execute(query, (title, clean_time, user_id))
    db.commit()

def remove_task(db, task_id):          
    c = db.cursor()                                     
    query = """DELETE FROM Tasks WHERE id =?"""                                                           
    c.execute(query, (task_id,))           
    db.commit()
    return "Deleted Task: %d" %task_id 

def get_user(db, user_id):  
    """Gets a user dictionary out of the database given an id"""
    c = db.cursor()
    query = """SELECT * from Users WHERE id=? """
    c.execute(query, (user_id,))
    result= c.fetchone()
    fields = ["id", "email", "password", "name"] 
    return dict(zip(fields, result))

def call_users(db, user_id=None):  
    """Pulls out the entire user database"""
    c = db.cursor()
    
    if user_id==None: 
        query = """SELECT * from Users """
        c.execute(query )  
    else: 
        query= """ SELECT * from Users WHERE id= ? """ 
        c.execute(query, (user_id,))
    
    users=[] 
    rows= c.fetchall()

    for row in rows:
        user = dict(zip(["id", "email", "password", "name"], 
                row))
        users.append(user)
    return users

def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    c = db.cursor()
    time_stamp= str(datetime.datetime.now())
    clean_time = time_stamp[:16]
    query = """UPDATE Tasks SET completed_at= ? WHERE id=?   """
    c.execute(query, (clean_time, task_id,))
    result= c.fetchone()
    db.commit()
    return True

    # id INTEGER PRIMARY KEY,
    # title VARCHAR(64),
    # created_at DATETIME,
    # completed_at DATETIME,
    # user_id INTEGER
 
def get_tasks(db, user_id=None):
    """Get all the tasks matching the user_id, getting all the 
    tasks in the system if the user_id is not provided. 
    Returns the results as a list of dictionaries."""

    c = db.cursor()
    
    if user_id==None: 
        query = """SELECT * from TASKS """
        c.execute(query )  
    else: 
        query= """ SELECT * from TASKS WHERE id= ? """ 
        c.execute(query, (user_id,))
    
    tasks=[] 
    rows= c.fetchall()

    for row in rows:
        task = dict(zip(["id", "title", "created_at", "completed_at", "user_id"], 
                row))
        tasks.append(task)
    return tasks

def get_task(db, task_id):
    """Gets a single task, given its id.
    Returns a dictionary of the task data."""
    c = db.cursor()
     
    query= """ SELECT * from TASKS WHERE id= ? """ 
    c.execute(query, (task_id,))

    result= c.fetchone()
    fields = ["id", "title", "created_at", "completed_at", "user_id"] 
    dict1= dict(zip(fields, result))
    return result 

