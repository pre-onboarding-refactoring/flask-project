from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()


class Company(db.Model):
    __tablename__ = "companies"
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tags          = db.relationship(
        "Tag",
        secondary="companies_tags",
        # lazy="subquery",
        # backref=db.backref("companies", lazy=True),
        )


companies_tags = db.Table(
    "companies_tags",
    db.Column("id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("company_id", db.Integer, db.ForeignKey("companies.id"), nullable=False),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), nullable=False),
)


class Tag(db.Model):
    __tablename__ = "tags"
    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    lang = db.Column(db.String(32), nullable=False)


class CompanyName(db.Model):
    __tablename__ = "company_names"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.String(32), nullable=False)
    lang       = db.Column(db.String(32), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False) 
