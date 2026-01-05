from sqlalchemy import Column, Integer, String

if __name__ != '__main__':
    from .bd import Base
else:
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

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
        # Assuming password is hashed, use hashlib to check
        import hashlib
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email