from flask import Flask, render_template, redirect, url_for, request

despesas = [{'nome': 'despesa', 'valor': 464}]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", despesas=despesas)

@app.route("/add", methods=["POST"])
def add():
    despesa = request.form["despesa"]
    valor = request.form["valor"]
    despesas.append({'nome': despesa, 'valor': valor})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)