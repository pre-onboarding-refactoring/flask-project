from flask_restx import Resource
from flask import request

from company.models import *


class CompanyView(Resource):
    def get(self):
        pass

    def post(self):
        code = request.headers.get("x-wanted-language", "ko")
        data = request.get_json()

        companies_dict = list(data.get("company_name").items())

        company = db.session.query(CompanyName).filter_by(lang=companies_dict[0][0], name=companies_dict[0][1]).first()

        if company:
                return {"message": "ALREADY EXIST COMPANY"}, 404
        
        company = Company()
        db.session.add(company)
        db.session.commit()

        for lang, name in companies_dict:
            company_name = CompanyName(name=name, lang=lang, company_id=company.id)
            db.session.add(company_name)

        tag_list = []
        for tag in data.get("tags"):
            for lang, name in tag.get("tag_name").items():
                tag_obj = db.session.query(Tag).filter_by(lang=lang, name=name).first()

                if not tag_obj:
                    tag_obj = Tag(name=name, lang=lang)
                    db.session.add(tag_obj)
                    db.session.commit()
                
                if lang == code:
                    tag_list.append(name)

                companies_tags_query = companies_tags.insert().values(
                    company_id = company.id,
                    tag_id = tag_obj.id
                )
                db.session.execute(companies_tags_query)

        db.session.commit()

        return {"message": "SUCCESS", "company_name": data.get("company_name").get(code), "tags": tag_list}, 201
