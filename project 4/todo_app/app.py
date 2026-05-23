from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model: Class methods will interact directly with this table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'

# Route to display all tasks
@app.route('/')
def index():
    # Query all tasks from the database
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        # Create a new Todo object and save it directly to the database
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # Find the task by ID and remove it from the database
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

# Automatically create the database tables before running the app
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)