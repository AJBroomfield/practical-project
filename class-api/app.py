from flask import Flask
import random

app = Flask(__name__)


@app.route('/get_class', methods=['GET'])
def get_class():
    return random.choice(['Barbarian','Bard','Cleric','Driud','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)