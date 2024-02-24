from app.utils.database import db

class Animal_report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_number = db.Column(db.Integer, nullable=False)
    report_date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    explanation = db.Column(db.String(500), nullable=False)

    def as_dict(self):
        return{ 
            "id": self.id, 
            "report_number": self.report_number, 
            "report_date": self.report_date.strftime("%Y-%m-%d %H:%M:%S"), 
            "name": self.name, 
            "role": self.role, 
            "explanation": self.explanation
            }


# class Visitor_report(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     report_number = db.Column(db.Integer, nullable=False)
#     report_date = db.Column(db.Datetime, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     type_discussion = db.Column(db.String(100), nullable=False)
#     explanation = db.Column(db.String(500), nullable=False)

#     def as_dict(self):
#         return{ 
#             "id": self.id, 
#             "report_number": self.report_number, 
#             "report_date": self.report_date.strftime("%Y-%m-%d %H:%M:%S"), 
#             "name": self.name, 
#             "type_discussion": self.type_discussion, 
#             "explanation": self.explanation
#             }

# class Revenue_report(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     report_number = db.Column(db.Integer, nullable=False)
#     report_date = db.Column(db.Datetime, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     division = db.Column(db.String(100), nullable=False)
#     explanation = db.Column(db.String(500), nullable=False)
#     rev_cal = db.Column(db.Integer, nullable=False)

#     def as_dict(self):
#         return{ 
#             "id": self.id, 
#             "report_number": self.report_number, 
#             "report_date": self.report_date.strftime("%Y-%m-%d %H:%M:%S"), 
#             "name": self.name, 
#             "division": self.division, 
#             "explanation": self.explanation,
#             "revenue": self.rev_cal
#             }