from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    role = requests.get('http://class_api:5000/get_animal')
    race = requests.get('http://race_api:5000/get_noise')
    stats = requests.post('http://stat-api:5000/get_stat', data=(role.text,race.text))
    return render_template('index.html', animal=animal.text, noise=noise.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)