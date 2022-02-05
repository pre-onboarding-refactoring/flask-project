from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from company import config
from company.controller import Company_Info
from company.models import db

migrate = Migrate()

def create_app(test_db_url=None):
    app = Flask(__name__)

    if test_db_url:
        app.config["SQLALCHEMY_DATABASE_URI"] = test_db_url
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    else:
        app.config.from_object(config)
    
    db.init_app(app)
    db.app = app
    db.create_all()
    migrate.init_app(app, db)

    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
    api.add_namespace(Company_Info, "/companies")

    return app, db


if __name__ == '__main__':
    app = create_app()[0]
    app.run(host="0.0.0.0", port=6000, debug=True)
