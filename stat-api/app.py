from flask import Flask, request, jsonify
import random
from rollstats import stat_roller

app = Flask(__name__)

@app.route('/get_stats', methods=['POST'])
def get_stats():
    data=request.get_json()
    
    role=data["role"]
    race=data["race"]
    return jsonify(stat_roller(role,race))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)