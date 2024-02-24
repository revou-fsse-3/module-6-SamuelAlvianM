# from app.models.report_model.reports import Animal_report, Visitor_report, Revenue_report
# from app.utils.database import db

# class Reports_repo():

#     def get_list_reports(self):
#         animal_r = Animal_report.query.all()
#         visitor_r = Visitor_report.query.all()
#         revenue_r = Revenue_report.query.all()
#         return animal_r, visitor_r, revenue_r
    
#     def update_report(self, animal_r, visitor_r, revenue_r, id):
#         ar_obj = db.session.get(Animal_report, id)
#         ar_obj.report_number = animal_r.report_number
#         ar_obj.report_date = animal_r.report_date
#         ar_obj.name = animal_r.name
#         ar_obj.role = animal_r.role
#         ar_obj.explanation = animal_r.explanation


#         vr_obj = db.session.get(Visitor_report, id)
#         vr_obj.report_number = visitor_r.report_number
#         vr_obj.report_date = visitor_r.report_date
#         vr_obj.name = visitor_r.name
#         vr_obj.type_discussion = visitor_r.type_discussion
#         vr_obj.explanation = visitor_r.explanation


#         rr_obj = db.session.get(Revenue_report, id)
#         rr_obj.report_number = revenue_r.report_number
#         rr_obj.report_date = revenue_r.report_date
#         rr_obj.name = revenue_r.name
#         rr_obj.division = revenue_r.division
#         rr_obj.explanation = revenue_r.explanation
#         rr_obj.rev_cal = revenue_r.rev_cal

#         db.session.commit()
#         return ar_obj, rr_obj, vr_obj
    
#     def create_report(self, animal_r, visitor_r, revenue_r):

#         db.session.add(animal_r)
#         db.session.add(visitor_r)
#         db.session.add(revenue_r)
#         db.session.commit()
#         return animal_r, visitor_r, revenue_r
    
#     def search_report(self, name):
#         ar = Animal_report.query.filter(Animal_report.name.like(f"%{name}%")).all()
#         vr = Visitor_report.query.filter(Visitor_report.name.like(f"%{name}%")).all()
#         rr = Revenue_report.query.filter(Revenue_report.name.like(f"%{name}%")).all()

#         return ar, vr, rr
        

    

    
