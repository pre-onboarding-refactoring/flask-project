import pytest
import json

from app import create_app
from my_settings import TEST_DB_URL
from company.models import Company, CompanyName, Tag, companies_tags

db = create_app(TEST_DB_URL)[1]

@pytest.fixture
def client():
    app = create_app(TEST_DB_URL)[0]
    return app.test_client()

def setup_function():
    datas = [
        {"name": "라인", "lang": "ko"}, 
        {"name": "라인 프레쉬", "lang": "ko"}
    ]
    tags = ["태그_1", "태그_8", "태그_15"]
    
    for data in datas:
        company = Company()
        db.session.add(company)
        db.session.commit()

        company_name = CompanyName(name=data["name"], lang=data["lang"], company_id=company.id)
        db.session.add(company_name)

        for tag in tags:
            tag_obj = Tag.query.filter_by(name=tag, lang=data["lang"]).first()
            if not tag_obj:
                tag_obj = Tag(name=tag, lang=data["lang"])
                db.session.add(tag_obj)
                db.session.commit()

            companies_tags_query = companies_tags.insert().values(
                    company_id = company.id,
                    tag_id = tag_obj.id
                )
            db.session.execute(companies_tags_query)

        db.session.commit()

def teardown_function():
    [db.session.delete(company) for company in CompanyName.query.all()]
    db.session.commit()
    [company_tag.tags.clear() for company_tag in Company.query.all()]
    db.session.commit()
    [db.session.delete(tag) for tag in Tag.query.all()]
    db.session.commit()
    [db.session.delete(company) for company in Company.query.all()]
    db.session.commit()

def test_company_name_autocomplete(client):
    """
    1. 회사명 자동완성
    회사명의 일부만 들어가도 검색이 되어야 합니다.
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """

    resp = client.get('/companies/search', query_string=dict(query="라인"), headers=[("x-wanted-language", "ko")])
    searched_companies = json.loads(resp.data.decode("utf-8"))

    assert client.status_code == 200
    assert searched_companies == [
        {"company_name": "라인"},
        {"company_name": "라인 프레쉬"},
    ]

def test_company_search(client):
    """
    2. 회사 이름으로 회사 검색
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """

    resp = client.get(
        "/companies/라인", headers=[("x-wanted-language", "ko")]
    )

    company = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert company == {
        "company_name": "라인",
        "tags": [
            "태그_1",
            "태그_8",
            "태그_15",
        ],
    }

    # 검색된 회사가 없는경우 404를 리턴합니다.
    resp = client.get(
        "/companies/라연", headers=[("x-wanted-language", "ko")]
    )

    assert resp.status_code == 404

def test_new_company(client):
    """
    3.  새로운 회사 추가
    새로운 언어(tw)도 같이 추가 될 수 있습니다.
    저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = client.post(
        "/companies",
        json={
            "company_name": {
                "ko": "애플",
                "tw": "Apple",
                "en": "Apple",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers=[("x-wanted-language", "tw")],
    )

    company = json.loads(resp.data.decode("utf-8"))

    assert resp.status_code == 201
    assert company == {
        "company_name": "Apple",
        "tags": [
            "tag_1",
            "tag_8",
            "tag_15",
        ],
    }
