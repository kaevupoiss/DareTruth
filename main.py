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
    checked1 = ""
    checked2 = ""
    checked3 = ""
    checked4 = ""
    checked5 = ""
    level = ""
    tod = 'truths'

    if request.args.get('tod') == "Truth":
        tod = 'truths'
    elif request.args.get('tod') == "Dare":
        tod = 'dares'

    if request.args.get('level'):
        level = int(request.args.get('level'))
    randq = randint(0, 2)

    if level == 1:
        newdare = req_data['levels'][level - 1][tod][randq]
        checked1 = "checked"
    elif level == 2:
        newdare = req_data['levels'][level - 1][tod][randq]
        checked2 = "checked"
    elif level == 3:
        newdare = req_data['levels'][level - 1][tod][randq]
        checked3 = "checked"
    elif level == 4:
        newdare = req_data['levels'][level - 1][tod][randq]
        checked4 = "checked"
    elif level == 5:
        newdare = req_data['levels'][level - 1][tod][randq]
        checked5 = "checked"

    return render_template('main.html', newdare = newdare, checked1 = checked1, checked2 = checked2,  checked3 = checked3, checked4 = checked4, checked5 = checked5)

if __name__ == "__main__":
    app.run(debug=True)
