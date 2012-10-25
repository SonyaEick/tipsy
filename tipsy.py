"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/") 
def first(): 
    return "<html><body> Woo I'm tipsy </body></html> "

@app.route("/tasks/Susan")
def index():
    return render_template("index.html", user_name="Susan")

@app.route("/tasks")
def list_tasks():
    db= model.connect_db() 
    tasks_from_db= model.get_tasks(db, None) 
    return render_template("list_tasks.html", tasks= tasks_from_db)

@app.route("/new_task")
def new_task_box():
    db= model.connect_db()
    tasks_from_db= model.get_tasks(db, None) 
    users_from_db= model.call_users(db, None)
    return render_template("new_task.html", tasks= tasks_from_db, 
                            users= users_from_db)

@app.route("/save_task", methods=["POST"])    
def new_task():
    task_title= request.form['task_title']
    db = model.connect_db()
    # Assume that all tasks are attached to user 1.
    task_id = model.new_task(db, task_title, 1)
    return redirect("/new_task")


@app.route("/save_user", methods=["POST"])    
def new_user():
    user_name= request.form['user_name']
    email= request.form['user_email']
    db = model.connect_db()
    #new_user(db, email, password, name)
    user_id = model.new_user(db, email, None, user_name)
    return redirect("/new_task")

@app.route("/del_task", methods=["POST"])    
def del_task():
    del_title= request.form['del_title']
    db = model.connect_db()
    # Assume that all tasks are attached to user 1.
    task_id = model.remove_task(db, int(del_title))
    return redirect("/new_task")

@app.route("/del_user", methods=["POST"])    
def del_user():
    del_user= request.form['del_name']
    db = model.connect_db()
    # Assume that all tasks are attached to user 1.
    user_id = model.remove_user(db, int(del_user))
    return redirect("/new_task")

if __name__ == "__main__":
    app.run(debug=True)









