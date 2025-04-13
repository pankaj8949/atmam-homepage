from flask import Flask, render_template, send_from_directory
from email_handler import email_bp, mail
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Initialize mail with app
mail.init_app(app)

# Register blueprint
app.register_blueprint(email_bp)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, 'img/logo/favicon.ico', mimetype='image/x-icon')

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml', mimetype='application/xml')

@app.route("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, 'robots.txt', mimetype='text/plain')

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/services")
def Services():
    return render_template("service.html")

@app.route("/services/text-book-publication")
def TextBookPublication():
    return render_template("text-book-publication.html")

@app.route("/projects")
def Projects():
    return render_template("project.html")

@app.route("/contact") 
def Contact():
    return render_template("contact.html")

@app.route("/terms-conditions")
def TermsConditions():
    return render_template("terms-conditions.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, port=8000)