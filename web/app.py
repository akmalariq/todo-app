from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="todo_db",
        user="postgres",
        password="postgres"
    )
    return conn

def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, task, done FROM todos ORDER BY id;")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return todos

@app.route("/")
def index():
    return render_template("index.html", todos=get_todos())

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task", "").strip()
    if task:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO todos (task, done) VALUES (%s, false);", (task,))
        conn.commit()
        cur.close()
        conn.close()
    return render_template("todos.html", todos=get_todos())

@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET done = NOT done WHERE id = %s;", (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("todos.html", todos=get_todos())

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s;", (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("todos.html", todos=get_todos())

@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit(todo_id):
    new_task = request.form.get("task", "").strip()
    if new_task:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE todos SET task = %s WHERE id = %s;", (new_task, todo_id))
        conn.commit()
        cur.close()
        conn.close()
    return render_template("todos.html", todos=get_todos())
