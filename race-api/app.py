from flask import Flask
import random

app = Flask(__name__)


@app.route('/get_race', methods=['GET'])
def get_race():
    return random.choice(['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Teifling'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)