from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/services")
def Services():
    return render_template("service.html")

@app.route("/projects")
def Projects():
    return render_template("project.html")

@app.route("/contact") 
def Contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)