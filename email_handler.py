from flask import Blueprint, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

# Create Blueprint
email_bp = Blueprint('email', __name__)

# Initialize mail (will be configured in main.py)
mail = Mail()

@email_bp.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        # Get sender email and password from environment variables
        sender_email = os.getenv('MAIL_USERNAME')
        sender_password = os.getenv('MAIL_PASSWORD')
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "New Contact Form Submission - Atmam Edutech"
        msg['From'] = sender_email
        msg['To'] = "ls8290519977@gmail.com"  # Replace with your recipient email
        
        # Create plain text content
        text_content = f"""
        New Contact Form Submission

        Name: {data.get('name', 'Not provided')}
        Email: {data.get('email', 'Not provided')}
        Phone: {data.get('phone', 'Not provided')}
        Message: {data.get('message', 'Not provided')}
        """
        
        # Create HTML content
        html_content = f"""
        <h2>New Contact Form Submission</h2>
        <p><strong>Name:</strong> {data.get('name', 'Not provided')}</p>
        <p><strong>Email:</strong> {data.get('email', 'Not provided')}</p>
        <p><strong>Phone:</strong> {data.get('phone', 'Not provided')}</p>
        <p><strong>Message:</strong> {data.get('message', 'Not provided')}</p>
        """
        
        # Attach parts
        part1 = MIMEText(text_content, 'plain')
        part2 = MIMEText(html_content, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        # Connect to SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        
        # Send email
        smtp_server.send_message(msg)
        
        # Disconnect from server
        smtp_server.quit()
        
        return jsonify({
            "success": True,
            "message": "Email sent successfully!"
        })
    except Exception as e:
        # Make sure to disconnect from server if there's an error
        try:
            smtp_server.quit()
        except:
            pass
            
        print(f"Email error: {str(e)}")  # Add this line for debugging
        return jsonify({
            "success": False,
            "message": f"Failed to send email: {str(e)}"
        }), 500 