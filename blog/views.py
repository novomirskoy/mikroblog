from blog import app
from flask import redirect
from flask import render_template
from flask import flash
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
	return render_template("create.html", form = form)


@app.route("/edit")
def edit_post():
    return "edit post"


@app.route("/manage")
def manage():
    return render_template("manage.html")
