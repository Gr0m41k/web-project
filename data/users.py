import datetime

from flask_login import UserMixin
from sqlalchemy import orm
import sqlalchemy

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):

    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    news = orm.relationship("News", back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"



