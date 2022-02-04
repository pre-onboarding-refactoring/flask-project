import csv

from company.models import *
from app            import db

CSV_PATH_PRODUCTS = "wanted_temp_data.csv"


def insert_company_names():
    with open(CSV_PATH_PRODUCTS, newline="", encoding="utf8") as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            print(row)


insert_company_names()

# def insert_company_names():
#     with open(CSV_PATH_PRODUCTS, newline="", encoding="utf8") as csvfile:
#         data_reader = csv.DictReader(csvfile)
#         for row in data_reader:
#             company = Company(name=row["company_name"])
#             db.session.add(company)

#         db.session.commit()
#         print("Company data Successfullly Inserted!")


# def insert_country():
#     ko = Country(name="ko")
#     en = Country(name="en")
#     ja = Country(name="ja")
#     db.session.add(ko)
#     db.session.add(en)
#     db.session.add(ja)

#     db.session.commit()
#     print("Country data Successfullly Inserted!")


# def insert_tag():
#     with open(CSV_PATH_PRODUCTS, newline="", encoding="utf8") as csvfile:
#         data_reader = csv.DictReader(csvfile)
#         for row in data_reader:
#             if row["tag_name"] != "":
#                 tag = Tag(name=row["tag_name"])
#                 db.session.add(tag)

#         db.session.commit()
#         print("Tag data Successfullly Inserted!")


# def insert_company_countries():
#     ko = Country.query.filter_by(name="ko").first()
#     en = Country.query.filter_by(name="en").first()
#     ja = Country.query.filter_by(name="ja").first()

#     with open(CSV_PATH_PRODUCTS, newline="", encoding="utf8") as csvfile:
#         data_reader = csv.DictReader(csvfile)
#         for index, row in enumerate(data_reader):
#             if row["company_ko"] != "":
#                 company_created = company_countries.insert().values(
#                     company_id=index + 1,
#                     country_id=ko.id,
#                     translated_name=row["company_ko"],
#                 )
#                 db.session.execute(company_created)

#             if row["company_en"] != "":
#                 company_created = company_countries.insert().values(
#                     company_id=index + 1,
#                     country_id=en.id,
#                     translated_name=row["company_en"],
#                 )
#                 db.session.execute(company_created)

#             if row["company_ja"] != "":
#                 company_created = company_countries.insert().values(
#                     company_id=index + 1,
#                     country_id=ja.id,
#                     translated_name=row["company_ja"],
#                 )
#                 db.session.execute(company_created)

#         db.session.commit()


# def insert_company_tags():
#     with open(CSV_PATH_PRODUCTS, newline="", encoding="utf8") as csvfile:
#         data_reader = csv.DictReader(csvfile)
#         for index, row in enumerate(data_reader):
#             company = Company.query.get(index + 1)
#             tags = row["tag_ko"].split("|")

#             for tag in tags:
#                 tag_id = int(tag.split("_")[1])

#                 tag_created = company_tags.insert().values(
#                     company_id=company.id, tag_id=tag_id
#                 )
#                 db.session.execute(tag_created)

#         db.session.commit()


# def insert_country_tags():
#     ko = Country.query.filter_by(name="ko").first()
#     en = Country.query.filter_by(name="en").first()
#     ja = Country.query.filter_by(name="ja").first()

#     with open(CSV_PATH_PRODUCTS, newline="", encoding="utf8") as csvfile:
#         data_reader = csv.DictReader(csvfile)
#         for row in data_reader:
#             ko_tags = row["tag_ko"].split("|")
#             en_tags = row["tag_en"].split("|")
#             ja_tags = row["tag_ja"].split("|")

#             for tag in ko_tags:
#                 tag_id = int(tag.split("_")[1])

#                 created_tags = country_tags.insert().values(
#                     country_id=ko.id, tag_id=tag_id, translated_tag=tag
#                 )
#                 db.session.execute(created_tags)

#             for tag in en_tags:
#                 tag_id = int(tag.split("_")[1])

#                 created_tags = country_tags.insert().values(
#                     country_id=en.id, tag_id=tag_id, translated_tag=tag
#                 )
#                 db.session.execute(created_tags)

#             for tag in ja_tags:
#                 tag_id = int(tag.split("_")[1])

#                 created_tags = country_tags.insert().values(
#                     country_id=ja.id, tag_id=tag_id, translated_tag=tag
#                 )
#                 db.session.execute(created_tags)
            
#         db.session.commit()

# insert_company()
# insert_country()
# insert_tag()
# insert_company_countries()
# insert_company_tags()
# insert_country_tags()
