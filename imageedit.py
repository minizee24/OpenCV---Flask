from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index_img.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True, port=5003)