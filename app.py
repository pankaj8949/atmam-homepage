from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your Gmail address
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your Gmail app password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        # Configure email settings
        msg = Message(
            subject="New Contact Form Submission - Atmam Edutech",
            sender=app.config['MAIL_USERNAME'],
            recipients=["info@atmam.org"]  # Replace with your recipient email
        )
        
        # Create email content with HTML formatting
        msg.html = f"""
        <h2>New Contact Form Submission</h2>
        <p><strong>Name:</strong> {data.get('name', 'Not provided')}</p>
        <p><strong>Email:</strong> {data.get('email', 'Not provided')}</p>
        <p><strong>Phone:</strong> {data.get('phone', 'Not provided')}</p>
        <p><strong>Message:</strong> {data.get('message', 'Not provided')}</p>
        """
        
        # Also include plain text version
        msg.body = f"""
        New Contact Form Submission

        Name: {data.get('name', 'Not provided')}
        Email: {data.get('email', 'Not provided')}
        Phone: {data.get('phone', 'Not provided')}
        Message: {data.get('message', 'Not provided')}
        """
        
        # Send email
        mail.send(msg)
        
        return jsonify({
            "success": True,
            "message": "Email sent successfully!"
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Failed to send email: {str(e)}"
        }), 500 