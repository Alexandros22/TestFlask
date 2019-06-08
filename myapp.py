from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/alex")
def salvador():
    return "Hello, Alexandros!"

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='127.0.0.1', port=5050)
=======
    app.run(host='127.0.0.1', port=5050)
>>>>>>> origin/master
