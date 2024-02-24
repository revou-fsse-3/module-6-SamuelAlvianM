from app.repositories.reports_repo.ar_repo import Ar_repo
from app.models.report_model.reports import Animal_report


class Ar_Services:

    def __init__(self):
        self.ar_repo = Ar_repo()

    # get
    def get_animal_reports(self):
        animal_reports = self.ar_repo.get_list_animal_reports()

        return [animal_report.as_dict() for animal_report in animal_reports]
    
    # search
    def search_animal_report(self, name):
        animal_reports = self.animal_repo.search_animal_report(name)
        return[animal_report.as_dict() for animal_report in animal_reports]
    
    def create_animal_report(self, animal_report_data_dto):
        animal_report = Animal_report()

        animal_report.report_number = animal_report_data_dto.report_number
        animal_report.report_date = animal_report_data_dto.report_date
        animal_report.name = animal_report_data_dto.name
        animal_report.role = animal_report_data_dto.role
        animal_report.explanation = animal_report_data_dto.explanation
        return animal_report.as_dict()
    
    def update_animal_report (self, id, animal_report_data_dto):
        updated_animal_report = self.animal_report_repo.update_animal_report(id, animal_report_data_dto)
        return updated_animal_report.as_dict()