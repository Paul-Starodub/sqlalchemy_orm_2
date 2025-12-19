import random
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

# user = session.query(User).filter_by(id=1).one_or_none()
# print("users", users)

# user = users[0]
# print(user.name)
# user.name = "Jane"
# session.delete(user)
# session.commit()


# names = ["Andrew", "John", "Jane", "Bob"]
# ages = [20, 30, 25, 20, 22, 24, 21, 28, 60]
#
# for x in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)
#
# session.commit()

# users = session.query(User).order_by(User.age.desc(), User.name).all()
# print(users)
