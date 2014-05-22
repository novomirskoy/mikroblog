from blog import app
from flask import redirect
from flask import render_template
from flask import flash
from flask import request
from flask import session
from flask import url_for
from blog.forms import *
from blog.models import *


@app.route("/")
@app.route("/index")
def index():
    posts = Post.select().order_by(Post.id.desc())
    return render_template("index.html",
                           posts=posts)


@app.route("/create", methods=['GET', 'POST'])
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post()
        post.name = request.form["name"]
        post.text = request.form["text"]
        post.save()
        flash("Запись " + request.form['name'] + " добавлена")
        return redirect("/index")
    return render_template("create.html", form=form, id=id)


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_post(id):
    post = Post.select().where(Post.id == id).get()
    form = CreatePostForm()
    form.name.data = post.name
    form.text.data = post.text
    if form.validate_on_submit():
        post.name = request.form["name"]
        post.text = request.form["text"]
        post.save()
        flash("Запись " + request.form['name'] + " обновлена")
        return redirect("/index")
    return render_template("create.html", form=form)


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
