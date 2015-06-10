import orm
from models import User, Blog, Comment

def test():
    yield from orm.create_pool(user='py3_webapp', password='py3_webapp', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='123', image='about:blank')

    yield from u.save()

for x in test():
    pass
