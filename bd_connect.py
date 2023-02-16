from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


DATABASE = {
    'drivername': 'driver://user:pass@localhost/database', #Тут можно использовать MySQL
    # или другой драйвер
    'host': 'localhost',
    'port': '5432',
    'username': 'youuser',
    'password': 'youpassword',
    'database': 'youdb'
}
DeclaraticeBase = declarative_base()

class Post(DeclaraticeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)

    def __repr__(self):
        return "".format(self.code)


from sqlalchemy.orm import sessionmaker


def db_connect():
    engine = create_engine('sqlite+pysqlite:///sqlite.bd')
    DeclaraticeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

if __name__ == '__main__':
    db_connect()