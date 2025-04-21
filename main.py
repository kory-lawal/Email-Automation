import os
import smtplib
import csv
from email.message import EmailMessage
from email.utils import make_msgid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Path to your logo
LOGO_PATH = "TBHlogo.jpg"

# Optional: Path to any file you want to attach
ATTACHMENT_PATH = "Algorithm-and-Flow-Chart (1).pdf" 

# Read recipients from CSV
with open("recipients.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['name']
        email = row['email']

        msg = EmailMessage()
        msg['Subject'] = "🎉 Welcome to TechBeginnersHub!"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email

        # Embed the image
        logo_cid = make_msgid(domain='tbh.local')
        logo_cid_str = logo_cid[1:-1]  # strip < >

        # HTML content
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2>Hi {name},</h2>
                <p>🎉 Welcome to <strong>TechBeginnersHub</strong>!</p>
                <p>We're thrilled to have you on board. At <strong>TBH</strong>, we believe in empowering beginners to build strong foundations in tech 🚀.</p>
                <p>Here's what you can expect:</p>
                <ul>
                    <li>💻 Hands-on Web & Mobile Dev training</li>
                    <li>🎓 Real-world projects and internship support</li>
                    <li>🤝 Mentorship from experienced developers</li>
                    <li>📚 Community, growth, and tech exposure</li>
                </ul>
                <p>Let’s build the future together ✨</p>
                <br/>
                <center><img src="cid:{logo_cid_str}" alt="TechBeginnersHub Logo" width="250"/></center>
                <p style="margin-top: 20px;">Best,<br/>Solih Akorede Lawal<br/>Founder, TechBeginnersHub</p>
            </body>
        </html>
        """
        msg.add_alternative(html_content, subtype='html')

        # Add image as inline content
        with open(LOGO_PATH, 'rb') as img:
            msg.get_payload()[0].add_related(img.read(), maintype='image', subtype='jpeg', cid=logo_cid)

        # Add file attachment (if specified)
        if ATTACHMENT_PATH:
            try:
                with open(ATTACHMENT_PATH, 'rb') as file:
                    file_name = os.path.basename(ATTACHMENT_PATH)
                    msg.add_attachment(file.read(), maintype='application', subtype='octet-stream', filename=file_name)
                    print(f"📎 Attachment '{file_name}' added.")
            except Exception as e:
                print("❌ Failed to add attachment:", e)

        # Send the email
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
                print(f"✅ Email sent to {name} ({email})")
        except Exception as e:
            print(f"❌ Failed to send to {name} ({email}):", e)
