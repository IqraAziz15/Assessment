from flask import Flask, request, jsonify, Blueprint, json
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwerty12@localhost/flasktask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
print(db)

apiroutes = Blueprint('apiroutes', __name__, url_prefix='/api')

class tableone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iso = db.Column(db.String(70), nullable=False)
    name = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return "id: %s, iso: %s, name: %s \n" % (self.id, self.iso, self.name)

class tabletwo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active_cases_critical_percentage = db.Column(db.String(70), nullable=False)
    active_cases_mild_percentage = db.Column(db.String(70), nullable=False)
    cases_with_outcome = db.Column(db.String(70), nullable=False)
    closed_cases_death_percentage = db.Column(db.String(70), nullable=False)
    closed_cases_recovered_percentage = db.Column(db.String(70), nullable=False)
    critical_condition_active_cases = db.Column(db.String(70), nullable=False)
    currently_infected = db.Column(db.String(70), nullable=False)
    death_cases = db.Column(db.String(70), nullable=False)
    death_closed_cases = db.Column(db.String(70), nullable=False)
    general_death_rate = db.Column(db.String(70), nullable=False)
    last_update = db.Column(db.String(70), nullable=False)
    mild_condition_active_cases = db.Column(db.String(70), nullable=False)
    recovered_closed_cases = db.Column(db.String(70), nullable=False)
    recovery_cases = db.Column(db.String(70), nullable=False)
    total_cases = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return """id: %s, active_cases_critical_percentage: %s, active_cases_mild_percentage: %s, 
        cases_with_outcome: %s, closed_cases_death_percentage: %s, closed_cases_recovered_percentage: %s, 
        critical_condition_active_cases: %s, currently_infected: %s, death_cases: %s, death_closed_cases: %s,
        general_death_rate: %s, last_update: %s, mild_condition_active_cases: %s, recovered_closed_cases: %s,
        recovery_cases: %s, total_cases: %s \n""" % (self.id, self.active_cases_critical_percentage, self.active_cases_mild_percentage,
        self.cases_with_outcome, self.closed_cases_death_percentage, self.closed_cases_recovered_percentage,
        self.critical_condition_active_cases, self.currently_infected, self.death_cases,self.death_closed_cases,
        self.general_death_rate, self.last_update, self.mild_condition_active_cases, self.recovered_closed_cases,
        self.recovery_cases, self.total_cases
        )

class tablethree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codeValue = db.Column(db.String(70), nullable=False)
    isPrivate = db.Column(db.String(70), nullable=False)
    name = db.Column(db.String(70), nullable=False)
    reference = db.Column(db.String(70), nullable=False)
    revisionNumber = db.Column(db.String(70), nullable=False)
    uri = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return """id: %s, codeValue: %s, isPrivate: %s, name: %s, reference: %s, revisionNumber: %s, uri: %s \n""" % (self.id, self.codeValue, self.isPrivate, self.name, self.reference, self.revisionNumber, self.uri)
    
@apiroutes.route('/fetchapidata', methods=['GET'])
def newapi():
    apireq = requests.get('https://covid-api.com/api/regions')
    jsondata = apireq.json()

    for i in jsondata['data']:
        entry = tableone(iso=i['iso'], name=i['name'])
        db.session.add(entry)
    db.session.commit()
    tableone.query.all()

    return jsondata
     
@apiroutes.route('/fetchapi2data', methods=['GET'])
def apitwo():
    apireq = requests.get('https://corona-virus-stats.herokuapp.com/api/v1/cases/general-stats')
    jsondata = apireq.json()

    entry = tabletwo(
    active_cases_critical_percentage = jsondata['data']['active_cases_critical_percentage'],
    active_cases_mild_percentage = jsondata['data']['active_cases_mild_percentage'],
    cases_with_outcome = jsondata['data']['cases_with_outcome'],
    closed_cases_death_percentage = jsondata['data']['closed_cases_death_percentage'],
    closed_cases_recovered_percentage = jsondata['data']['closed_cases_recovered_percentage'],
    critical_condition_active_cases = jsondata['data']['critical_condition_active_cases'],
    currently_infected = jsondata['data']['currently_infected'],
    death_cases = jsondata['data']['death_cases'],
    death_closed_cases = jsondata['data']['death_closed_cases'],
    general_death_rate = jsondata['data']['general_death_rate'],
    last_update = jsondata['data']['last_update'],
    mild_condition_active_cases = jsondata['data']['mild_condition_active_cases'],
    recovered_closed_cases = jsondata['data']['recovered_closed_cases'],
    recovery_cases = jsondata['data']['recovery_cases'],
    total_cases = jsondata['data']['total_cases'])
    db.session.add(entry)
    db.session.commit()
    tabletwo.query.all()

    return jsondata

@apiroutes.route('/fetchapi3data', methods=['GET'])
def index():
    req = requests.get('http://covid19.richdataservices.com/rds/api/catalog/int/jhu_country/metadata/json')
    jsondata = req.json()

    for i in jsondata['classifications'][0]['codes']:
        entry = tablethree(
            codeValue = i['codeValue'],
            isPrivate = i['isPrivate'],
            name = i['name'],
            reference = i['reference'],
            revisionNumber = i['revisionNumber'],
            uri = i['uri'])
        db.session.add(entry)
    db.session.commit()
    tablethree.query.all() 

    return jsondata

@apiroutes.route('/getdatafromdb', methods=['GET'])
def getdata():
    gettableone = tableone.query.all()
    datatb1 = (gettableone)
    gettabletwo = tabletwo.query.all()
    datatb2 = (gettabletwo)
    gettablethree = tablethree.query.all()
    datatb3 = (gettablethree)
    cumulativelist = datatb1 +datatb2 +datatb3
    return str(cumulativelist)



if __name__ == "__main__":
    manager.run()
    db.create_all()
