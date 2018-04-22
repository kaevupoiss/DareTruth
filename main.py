from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def dare():
    newdare = ""
    checked = ""
    level = request.args.get('level')
    if level == "1":
        newdare = "Karmel on tore"
        checked = "checked"
    return render_template('main.html', newdare = newdare, checked = checked)

if __name__ == "__main__":
    app.run()
