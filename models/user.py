from sqlalchemy import Column, Integer, String
from .bd import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

    def check_password(self, password):
        import hashlib
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email