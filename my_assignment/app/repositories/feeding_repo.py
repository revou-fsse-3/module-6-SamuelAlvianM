from app.models.feeding import Feeding
from app.utils.database import db

class Feeding_repo:
    def get_list_feeding(self):
        feeds = Feeding.query.all()
        return feeds
    
    def update_feeding(self, id, feeds):
        feeds_obj = Feeding.query.get(id)
        if feeds_obj:
            feeds_obj.name = feeds.name
            feeds_obj.feeding_time = feeds.feeding_time
            feeds_obj.food_count_kg = feeds.food_count_kg
            feeds_obj.food_type = feeds.food_type
            
            db.session.commit()
            return feeds_obj
        return None
    
    def search_feeding(self, name):
        feeds = Feeding.query.filter(Feeding.name.like(f"%{name}%")).all()
        return feeds
    
    def delete_feeding(self, id):
        feeds_obj = Feeding.query.get(id)
        if feeds_obj:
            db.session.delete(feeds_obj)
            db.session.commit()
            return True
        return False
