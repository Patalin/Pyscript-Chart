from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def pyscript_test():
  return render_template("calculator-pyscript.html")


if __name__ == "__main__":
  app.run(debug=True)