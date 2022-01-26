from flask_restx import Resource
from flask import request

from company.models import *


class CompanyView(Resource):
    def get(self):
        pass

    def post(self):
        code = request.headers.get("x-wanted-language", "ko")
        data = request.get_json()

        company_name_list = data.get("company_name")

        company = Company()
        db.session.add(company)
        db.session.commit()

        for code, name in company_name_list.items():
            company_name = CompanyName(name=name, lang=code, company_id=company.id)
            db.session.add(company_name)

        tags = data.get("tags")

        for tag in tags:
            for lang, name in tag["tag_name"].items():
                tag_obj = db.session.query(Tag).filter_by(lang=lang, name=name).first()

                if not tag_obj:
                    tag_obj = Tag(name=name, lang=lang)
                    db.session.add(tag_obj)

                companies_tags_query = companies_tags.insert().values(
                    company_id = company.id,
                    tag_id = tag_obj.id
                )
                db.session.execute(companies_tags_query)

        db.session.commit()

        return {"message": "SUCCESS"}, 201
