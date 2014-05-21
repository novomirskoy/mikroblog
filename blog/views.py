from blog import app
from flask import redirect
from flask import render_template
from flask import flash
from flask import request
from flask import session
from flask import url_for
from blog.forms import *


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/create", methods=('GET', 'POST'))
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        flash("Новая запись успешно добавлена")
        return redirect("/index")
    return render_template("create.html", form=form)


@app.route("/edit")
def edit_post():
    return "edit post"


@app.route("/manage")
def manage():
    return render_template("manage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm()

    if form.validate_on_submit():
        if request.form["username"] != app.config["USERNAME"]:
            error = "Неверное имя пользователя"
        elif request.form["password"] != app.config["PASSWORD"]:
            error = "Неверный пароль"
        else:
            session["logged_in"] = True
            flash("Вы выполнили вход")
            return redirect(url_for("index"))

    return render_template("login.html", form=form, error=error)


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Вы вышли")

    return redirect(url_for("index"))
