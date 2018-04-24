from flask import Flask, render_template, request
from random import randint
import json
app = Flask(__name__)

def get_dares():
    with open("dares.json", "rb") as dares:
        return json.load(dares)

@app.route("/")
def dare():
    req_data = get_dares()
    maxitem = 0
    newdare = ""
    checked = {
        "1": False,
        "2": False,
        "3": False,
        "4": False,
        "5": False
    }

    tod = 'truths'
    if request.args.get('tod') == "Truth":
        tod = 'truths'
    elif request.args.get('tod') == "Dare":
        tod = 'dares'


    randq = randint(0, maxitem)
    level = ""
    if request.args.get('level'):
        level = int(request.args.get('level'))
        maxitem = len(req_data['levels'][level - 1][tod]) - 1
        randq = randint(0, maxitem)
        newdare = req_data['levels'][level - 1][tod][randq]
        checked[str(level)] = True
    randq = randint(0, 2)

    return render_template('main.html', newdare = newdare, checked = checked)

if __name__ == "__main__":
    app.run(debug=True)
