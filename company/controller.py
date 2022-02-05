import string

from flask_restx import Resource, Namespace
from flask import request

from company.models import *

Company_Info = Namespace("About Company", description="회사 정보 info")

@Company_Info.route('/search')
class CompanySearchView(Resource):
    def get(self):

        code = request.headers.get("x-wanted-language", "ko")
        company_name = request.args.get("query")
    
        if company_name == "":
            return {"message" : "KEY ERROR"}, 404
        
        company_name_datas = db.session.query(CompanyName).filter(CompanyName.name.like(f"%{company_name}%"), CompanyName.lang==code).all()
        
        if not company_name_datas:
            return {"message" : "COMPANY NOT FOUND"}, 404
        
        result = [
            {"company_name" : company_name.name}
            for company_name in company_name_datas
        ]

        return result, 200


@Company_Info.route('')
class CompanyInfoView(Resource):
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

        return {"company_name": data.get("company_name").get(code), "tags": tag_list}, 201


@Company_Info.route('/<company_name>')
class CompanyDetailView(Resource):
    def get(self, company_name):
        code = request.headers.get("x-wanted-language")

        company = CompanyName.query.filter_by(name=string.capwords(company_name), lang=code).first()

        if company is None:
            return {"message": "NOT FOUND COMPANY"}, 404

        tag_list = []
        for com_tag in db.session.query(companies_tags).filter_by(company_id=company.company_id):
            for tag in Tag.query.filter_by(id=com_tag.tag_id):
                if tag.lang == code:
                    tag_list.append(tag.name)

        return {"company_name": string.capwords(company_name), "tags": tag_list}, 200
