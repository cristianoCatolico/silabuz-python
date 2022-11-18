from flask import Flask, render_template, flash, redirect, abort, jsonify
from config import *
from app.forms.loginForm import *
from app.forms.studentForm import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from flask_login import (
    LoginManager,
    logout_user,
    login_required,
    current_user,
    login_user,
)

from app import create_app

load_dotenv()

app = create_app()

login= LoginManager(app)
login.login_view = 'login'

@app.route('/')
@login_required
def main():
    return render_template('index.html') 

from models.User import User, Permission
from models.Post import Post
@app.route('/login', methods= ['GET', 'POST'])
def login():
    if current_user.is_autenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        return redirect(url_for('index'))
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

from models.Alumno import Alumno
@app.route('/students', methods=['GET'])
def students():
    # obtener la lista de estudiantes
    students =Alumno.query_all()
    return render_template('students.html', students = students )

@app.route('/save-student', methods=['GET','POST'])
def save_student():
    student = None
    formStudent = StudentForm()
    if formStudent.validate_on_submit():
        student = Alumno.query.filter_by(dni=formStudent.dni.data)
        if student is None:
            student = Alumno(nombre=formStudent.name.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/students')
    return render_template('student/edit-student.html',form=formStudent)

from decorator import admin_required,permission_required

@app.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "Para admins!"


@app.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "Para comentarios de moderadores!"

@app.route('/update-student/<dni>')
def update_student(dni):
    # retornar los datos del estudiante con el campo dni y llenarlos en el formulario.
    try:
        student = ''
    except:
        abort(500)
    return render_template("update_student.html",data=data)

@app.route('/salon')
def save_classroom():
    return jsonify({'message': 'under implementation'})

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__== '__main__':
    app.run(debug=True)
