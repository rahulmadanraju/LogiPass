from flask import Flask, jsonify, render_template, request, redirect, url_for
from main import password_gen

app = Flask(__name__, static_folder="static")


@app.route("/", methods=["GET", "POST"])
def my_func():
    if request.method == "POST":
        output = password_gen(password_length=12)
        return render_template("index.html", output=output)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
