from flask import Flask
from models.user import User
from models.bd import SessionLocal, create_tables, hash_password
from routes import auth_bp, contact_bp, courses_bp

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

app.register_blueprint(courses_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(contact_bp)

create_tables()

db = SessionLocal()
try:
    if not db.query(User).filter(User.username == 'admin').first():
        default_user = User(username='admin', password=hash_password('mudar123'), email='admin@example.com')
        db.add(default_user)
        db.commit()
finally:
    db.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
