from flask import Flask, render_template, request
from random import randint
import json
app = Flask(__name__)

def get_dares():
    return json.loads(open("dares.json").read())

@app.route("/")
def dare():
    req_data = get_dares()
    newdare = ""
    checked1 = ""
    checked2 = ""
    checked3 = ""
    level = ""
    if request.args.get('level'):
        level = int(request.args.get('level'))
    randq = randint(0, 2)
    if level == 1:
        newdare = req_data['levels'][level - 1]['dares'][randq]
        checked1 = "checked"
    elif level == 2:
        newdare = req_data['levels'][level - 1]['dares'][randq]
        checked2 = "checked"
    elif level == 3:
        newdare = req_data['levels'][level - 1]['dares'][randq]
        checked3 = "checked"
    return render_template('main.html', newdare = newdare, checked1 = checked1, checked2 = checked2,  checked3 = checked3)

if __name__ == "__main__":
    app.run(debug=True)
