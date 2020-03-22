from data import db_session
from data.users import User
db_session.global_init("db/blogs.sqlite")

session = db_session.create_session()

session.query(User).filter(User.id >= 3).delete()
session.commit()