from app.utils.database import db

class Feeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    feeding_time = db.Column(db.DateTime, nullable=False)
    food_count_kg = db.Column(db.Integer, nullable=True)
    food_type = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "feeding_time": self.feeding_time.strftime("%Y-%m-%d %H:%M:%S"),
            "food_count_kg": self.food_count_kg,
            "food_type": self.food_type
        }
    
    def __str__(self) -> str:
        return f"{self.name}"
