from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    role = requests.get('http://class_api:5000/get_class')
    race = requests.get('http://race_api:5000/get_race')
    role_race = {"role":role.text , "race":race.text}
    stats = requests.post('http://stat_api:5000/get_stats', json=(role_race))
    return render_template('index.html', role=role.text, race=race.text, stats=stats.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)