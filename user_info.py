from data import db_session
from data.users import User
db_session.global_init("db/blogs.sqlite")

session = db_session.create_session()
user = session.query(User).first()
print(user.name)

for user in session.query(User).all():
    print(user)

for user in session.query(User).filter(User.id > 1, User.email.notilike("%4%")):
    print(user)

for user in session.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
    print(user)