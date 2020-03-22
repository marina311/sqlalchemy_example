from data import db_session
from data.users import User
db_session.global_init("db/blogs.sqlite")

user = User()
user.name = "Пользователь 3"
user.about = "биография пользователя 4"
user.email = "email4@email.ru"
session = db_session.create_session()
session.add(user)
session.commit()