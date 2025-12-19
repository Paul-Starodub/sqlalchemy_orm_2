from sqlalchemy.orm import sessionmaker
from models import User, engine


Session = sessionmaker(bind=engine)
session = Session()

# user = User(name="John", age=30)
# user_2 = User(name="Jane", age=25)
# user_3 = User(name="Bob", age=20)
# user_4 = User(name="Alice", age=22)
# session.add_all([user_3, user_4])
# session.add(user_2)
# session.commit()

users = session.query(User).all()
print("users", users)
