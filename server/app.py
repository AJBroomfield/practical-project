from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import requests
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 

db = SQLAlchemy(app)



class PlayerInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(15))
    role = db.Column(db.String(15))
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    
db.create_all()

@app.route('/')
def home():
    role = requests.get('http://class_api:5000/get_class')
    race = requests.get('http://race_api:5000/get_race')
    role_race = {"role":role.text , "race":race.text}
    stats = requests.post('http://stat_api:5000/get_stats', json=(role_race))
    statinfo= stats.json()
    db_info = PlayerInfo(
        race = race.text, 
        role = role.text, 
        strength = statinfo["STR"],
        dexterity = statinfo["DEX"],
        constitution = statinfo["CON"],
        intelligence = statinfo["INT"],
        wisdom = statinfo["WIS"],
        charisma = statinfo["CHA"]
        )
    db.session.add(db_info)
    db.session.commit()
    
    groupstat = PlayerInfo.query.order_by(desc(PlayerInfo.id)).limit(5).all()

    return render_template('index.html', role=role.text, race=race.text, stats=statinfo, groupstat=groupstat)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)