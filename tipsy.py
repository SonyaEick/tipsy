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
    return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])    
def new_task():
    task_title= request.form['task_title']
    db = model.connect_db()
    # Assume that all tasks are attached to user 1.
    task_id = model.new_task(db, task_title, 1)
    return redirect("/tasks")

if __name__ == "__main__":
    app.run(debug=True)
