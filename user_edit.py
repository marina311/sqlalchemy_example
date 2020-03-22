import datetime
from data import db_session
from data.users import User
db_session.global_init("db/blogs.sqlite")

session = db_session.create_session()

user = session.query(User).filter(User.id == 3).first()
print(user)
user.name = "Измененное имя пользователя"
user.created_date = datetime.datetime.now()
session.commit()