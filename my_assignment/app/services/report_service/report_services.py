# from app.repositories.reports_repo.report_repo import Reports_repo
# from app.models.report_model.reports import Animal_report, Revenue_report, Visitor_report


# class Report_Services:

#     def __init__(self):
#         self.reports_repo = Reports_repo()

#     # get
#     def get_animal_reports(self):
#         animal_reports = self.reports_repo.get_list_animal_report()

#         return [animal_report.as_dict() for animal_report in animal_reports]

#     def get_animal_reports(self):
#         visitor_reports = self.reports_repo.get_list_visitor_report()

#         return [visitor_report.as_dict() for visitor_report in visitor_reports]
    
#     def get_revenue_reports(self):
#         revenue_reports = self.reports_repo.get_list_revenue_report()

#         return [revenue_report.as_dict() for revenue_report in revenue_reports]   

#     # search
#     def search_animal_report(self, name):
#         animal_reports = self.animal_repo.search_animal_report(name)
#         return[animal_report.as_dict() for animal_report in animal_reports]
    
#     def search_visitor_report(self, name):
#         visitor_reports = self.visitor_repo.search_visitor_report(name)
#         return[visitor_report.as_dict() for visitor_report in visitor_reports]
    
#     def search_revenue_report(self, name):
#         revenue_reports = self.revenue_repo.search_revenue_report(name)
#         return[revenue_report.as_dict() for revenue_report in revenue_reports]
    

#     # create
#     def create_animal_report(self, animal_report_data_dto):
#         animal_report = Animal_report()

#         animal_report.report_number = animal_report_data_dto.report_number
#         animal_report.report_date = animal_report_data_dto.report_date
#         animal_report.name = animal_report_data_dto.name
#         animal_report.role = animal_report_data_dto.role
#         animal_report.explanation = animal_report_data_dto.explanation
#         return animal_report.as_dict()

#     def create_visitor_report(self, visitor_report_data_dto):
#         visitor_report = Visitor_report()

#         visitor_report.report_number = visitor_report_data_dto.report_number
#         visitor_report.report_date = visitor_report_data_dto.report_date
#         visitor_report.name = visitor_report_data_dto.name
#         visitor_report.type_discussion = visitor_report_data_dto.type_discussion
#         visitor_report.explanation = visitor_report_data_dto.explanation
#         return visitor_report.as_dict()
    
#     def create_revenue_report(self, revenue_report_data_dto):
#         revenue_report = Revenue_report()

#         revenue_report.report_number = revenue_report_data_dto.report_number
#         revenue_report.report_date = revenue_report_data_dto.report_date
#         revenue_report.name = revenue_report_data_dto.name
#         revenue_report.division = revenue_report_data_dto.division
#         revenue_report.explanation = revenue_report_data_dto.explanation
#         revenue_report.rev_cal = revenue_report_data_dto.rev_cal
#         return revenue_report.as_dict()
    
#     # update
#     def update_animal_report (self, id, animal_report_data_dto):
#         updated_animal_report = self.animal_report_repo.update_animal_report(id, animal_report_data_dto)
#         return updated_animal_report.as_dict()
    
#     def update_visitor_report (self, id, visitor_report_data_dto):
#         updated_visitor_report = self.visitor_report_repo.update_visitor_report(id, visitor_report_data_dto)
#         return updated_visitor_report.as_dict()

#     def update_revenue_report (self, id, revenue_report_data_dto):
#         updated_revenue_report = self.revenue_report_repo.update_revenue_report(id, revenue_report_data_dto)
#         return updated_revenue_report.as_dict()
        
