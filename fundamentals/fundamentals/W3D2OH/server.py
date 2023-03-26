from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<string:name>/<int:number>")
def index(name,number):
    return render_template("index.html", name=name, number=number)

@app.route("/coding/dojo/rules")
def hello():
    return "Hello Awesome Developer"

if __name__ == "__main__":
    app.run(debug=True)
