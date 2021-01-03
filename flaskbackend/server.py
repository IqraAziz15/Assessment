from api import coronaapiroutes
from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwerty12@localhost/flasktask'
db = SQLAlchemy(app)
app.register_blueprint(coronaapiroutes.apiroutes)

if __name__ == "__main__":
    app.run(debug=True)