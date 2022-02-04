from flask            import Flask
from flask_restx      import Api
from flask_migrate    import Migrate

from company.controller import *
from company.models import db
from config import DB_URL


def create_app():

    app = Flask(__name__)
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")

    app.config["SQLALCHEMY_DATABASE_URI"]        = DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    
    api.add_namespace(Company, "/companies")
    
    return app

migrate = Migrate(create_app, db)

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=6000, debug=True)
