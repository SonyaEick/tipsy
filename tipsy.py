"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, redirect, request, session, g
import model
import datetime

app = Flask(__name__)
# SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.before_request
def set_up_db():
    g.db = model.connect_db()

@app.teardown_request
def disconnect_db(exception):
    g.db.close()

@app.route("/set_date")
def set_date():
    session['date'] = datetime.datetime.now()
    return "Date set"

@app.route("/get_date")
def get_date():
    return str(session['date'])

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def index():
    return render_template("index.html", user_name="chriszf")

@app.route("/save_task", methods=["POST", "GET"])
def save_task():
    title = request.form['task_title']
    model.new_task(g.db, title)
    return redirect("/tasks")

@app.route("/tasks")
def list_tasks():
    user_id = session.get("user_id", None)
    tasks_from_db = model.get_tasks(g.db, None)
    users_from_db= model.call_users(g.db, None)
    return render_template("list_tasks.html", tasks=tasks_from_db, 
        users= users_from_db)

@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
    task_from_db = model.get_task(g.db, id)
    return render_template("view_task.html", task=task_from_db)

@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
    model.complete_task(g.db, id)
    return redirect("/tasks")


@app.route("/authenticate", methods=["POST", "GET"])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    user_id = model.authenticate(g.db, email, password)
    session['user_id'] = user_id
    return redirect("/tasks")

# THis is the OLD MODEL.py here below#

# @app.route("/new_task")
# def new_task_box():
#     tasks_from_db= model.get_tasks(g.db, None) 
#     users_from_db= model.call_users(g.db, None)
#     return render_template("list_tasks.html", tasks= tasks_from_db, 
#                             users= users_from_db)

@app.route("/save_task", methods=["POST"])    
def new_task():
    task_title= request.form['task_title']
    # Assume that all tasks are attached to user 1.
    task_id = model.new_task(g.db, task_title, 1)
    return redirect("/tasks")

@app.route("/save_user", methods=["POST"])    
def new_user():
    user_name= request.form['user_name']
    email= request.form['user_email']
    #new_user(db, email, password, name)
    user_id = model.new_user(g.db, email, None, user_name)
    return redirect("/tasks")

@app.route("/del_task", methods=["POST"])    
def del_task():
    del_title= request.form['del_title']
    # Assume that all tasks are attached to user 1.
    task_id = model.remove_task(g.db, int(del_title))
    return redirect("/tasks")

@app.route("/del_user", methods=["POST"])    
def del_user():
    del_user= request.form['del_name']
    # Assume that all tasks are attached to user 1.
    user_id = model.remove_user(g.db, int(del_user))
    return redirect("/tasks")

if __name__ == "__main__":
    app.run(debug=True)