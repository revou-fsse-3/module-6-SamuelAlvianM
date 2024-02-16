from app.utils.database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=False)
    division = db.Column(db.String(100), nullable=False)



    def as_dict(self):
        return{ "id": self.id, "name": self.name, "age": self.age, "phone": self.phone, "gender": self.gender, "division": self.division}
    
    def __str__(self) -> str:
        return f"{self.name}"