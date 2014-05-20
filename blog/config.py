import os


basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog.db")
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")

DATABASE = {
	"name": "blog.db",
	"engine": "peewee.SqliteDatabase",
}

WTF_CSRF_ENABLED = True
SECRET_KEY = "blablublimblimblubla"