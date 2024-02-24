from app.models.report_model.reports import Animal_report
from app.utils.database import db

class Ar_repo():
    def get_list_animal_reports(self):
        animal_r = Animal_report.query.all()

        return animal_r
    
    def update_animal_report(self, animal_r, id):
        ar_obj = db.session.get(Animal_report, id)
        ar_obj.report_number = animal_r.report_number
        ar_obj.report_date = animal_r.report_date
        ar_obj.name = animal_r.name
        ar_obj.role = animal_r.role
        ar_obj.explanation = animal_r.explanation
    
        db.session.commit()
        return ar_obj
    
    def create_animal_report(self, animal_r):

        db.session.add(animal_r)
        db.session.commit()
        return animal_r
    
    def search_animal_report(self, name):
        ar = Animal_report.query.filter(Animal_report.name.like(f"%{name}%")).all()

        return ar