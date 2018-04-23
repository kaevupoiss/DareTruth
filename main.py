from flask import Flask, render_template, request
from random import randint
import json
app = Flask(__name__)

def get_dares():
    return json.loads(open("dares.json").read())

@app.route("/")
def dare():
    req_data = get_dares()
    randq = randint(0, 2)

    newdare = ""
    checked = {
        "1": False,
        "2": False,
        "3": False,
        "4": False,
        "5": False
    }
    level = ""
    tod = 'truths'

    if request.args.get('tod') == "Truth":
        tod = 'truths'
    elif request.args.get('tod') == "Dare":
        tod = 'dares'

    if request.args.get('level'):
        level = int(request.args.get('level'))
    randq = randint(0, 2)

    newdare = req_data['levels'][level - 1][tod][randq]
    checked[str(level)] = True

    return render_template('main.html', newdare = newdare, checked = checked)

if __name__ == "__main__":
    app.run(debug=True)
