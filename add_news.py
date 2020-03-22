from data import db_session
from data.news import News
from data.users import User
db_session.global_init("db/blogs.sqlite")
session = db_session.create_session()

news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
session.add(news)
session.commit()


user = session.query(User).filter(User.id == 1).first()
news = News(title="Вторая новость", content="Уже вторая запись!",
            user=user, is_private=False)
session.add(news)
session.commit()


user = session.query(User).filter(User.id == 1).first()
news = News(title="Личная запись", content="Эта запись личная",
            is_private=True)
user.news.append(news)
session.commit()