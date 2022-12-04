from flask import Flask, render_template
import json
from models.player import Player

app = Flask(__name__)

@app.route('/save_deaths/<int:deaths>')
def save_deaths(deaths):

    # Read the player's death count from the JSON file
    with open('deaths.json', 'r') as f:
        deaths_data = json.load(f)

    # Update the player's death count in the JSON file
    deaths_data['deaths'] = deaths
    with open('deaths.json', 'w') as f:
        json.dump(deaths_data, f)

    return render_template('deaths_saved.html', deaths=deaths)