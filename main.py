from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dare")
def dare():
    l1, l2, l3 = False, False, False
    newdare = ""
    if request.form.get('level1'):
        newdare = "Karmel on tore!"
    return render_template("dare.html", newdare = newdare)

if __name__ == "__main__":
    app.run()
