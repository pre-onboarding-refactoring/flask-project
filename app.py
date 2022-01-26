from flask            import Flask
from flask_restx      import Api
from flask_migrate    import Migrate

from company.controller import CompanyView
from company.models import db
from config import DB_URL


app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"]        = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
db.app = app
db.create_all()
migrate = Migrate(app, db)

api.add_resource(CompanyView, "/companies")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
