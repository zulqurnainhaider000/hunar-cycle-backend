import os
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def get_smtp_config():
    host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    port = int(os.getenv('SMTP_PORT', 587))
    user = os.getenv('SMTP_USER')
    password = os.getenv('SMTP_PASSWORD')
    return host, port, user, password

def generate_email_html(otp_code: str, recipient_email: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Email Verification - Hunar Cycle Academy</title>
      <style>
        body {{
          margin: 0;
          padding: 0;
          background-color: #0B1120;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
          color: #F8FAFC;
        }}
        .container {{
          max-width: 560px;
          margin: 30px auto;
          background-color: #0F172A;
          border: 1px solid #1E293B;
          border-radius: 16px;
          overflow: hidden;
          box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        }}
        .header {{
          background: linear-gradient(135deg, #0284C7 0%, #10B981 100%);
          padding: 32px 24px;
          text-align: center;
        }}
        .header h1 {{
          margin: 0;
          font-size: 24px;
          font-weight: 800;
          color: #FFFFFF;
          letter-spacing: 0.5px;
        }}
        .header p {{
          margin: 6px 0 0;
          font-size: 14px;
          color: #E2E8F0;
        }}
        .content {{
          padding: 36px 28px;
          text-align: center;
        }}
        .content h2 {{
          margin: 0 0 12px;
          font-size: 20px;
          color: #F8FAFC;
        }}
        .content p {{
          margin: 0 0 24px;
          font-size: 15px;
          line-height: 1.6;
          color: #94A3B8;
        }}
        .otp-box {{
          display: inline-block;
          background-color: #1E293B;
          border: 2px solid #38BDF8;
          border-radius: 12px;
          padding: 18px 36px;
          margin: 10px 0 28px;
        }}
        .otp-code {{
          font-family: 'Courier New', Courier, monospace;
          font-size: 38px;
          font-weight: 800;
          letter-spacing: 10px;
          color: #38BDF8;
          margin: 0;
        }}
        .badge {{
          display: inline-block;
          background-color: rgba(16, 185, 129, 0.15);
          color: #10B981;
          font-size: 13px;
          font-weight: 600;
          padding: 4px 12px;
          border-radius: 9999px;
          margin-bottom: 20px;
          border: 1px solid rgba(16, 185, 129, 0.3);
        }}
        .security-notice {{
          background-color: #1E293B;
          border-radius: 10px;
          padding: 16px;
          font-size: 13px;
          color: #94A3B8;
          text-align: left;
          line-height: 1.5;
          margin-top: 20px;
          border-left: 4px solid #F59E0B;
        }}
        .footer {{
          padding: 20px;
          text-align: center;
          font-size: 12px;
          color: #64748B;
          border-top: 1px solid #1E293B;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1>Hunar Cycle Academy</h1>
          <p>StudyMate &bull; Peer Skills &bull; Academic Excellence</p>
        </div>
        <div class="content">
          <div class="badge">&bull; 10-Minute Expiry &bull;</div>
          <h2>Verify Your Email Address</h2>
          <p>
            Welcome to Hunar Cycle Academy! Please enter the 6-digit verification code below in your mobile app to activate your account.
          </p>
          <div class="otp-box">
            <span class="otp-code">{otp_code}</span>
          </div>
          <div class="security-notice">
            <strong>Security Reminder:</strong>
            <br>&bull; This verification code expires in <strong>10 minutes</strong>.
            <br>&bull; Never share this one-time code with anyone.
            <br>&bull; If you did not create an account with Hunar Cycle Academy, you can safely disregard this email.
          </div>
        </div>
        <div class="footer">
          &copy; 2026 Hunar Cycle Academy / StudyMate. All rights reserved.
        </div>
      </div>
    </body>
    </html>
    """

def send_otp_email(recipient_email: str, otp_code: str) -> tuple[bool, str]:
    """
    Sends a 6-digit OTP verification code via Gmail SMTP (smtplib + email.mime).
    Returns (success: bool, message_or_error: str).
    """
    host, port, user, password = get_smtp_config()

    if not user or not password:
        err_msg = "[EmailService] SMTP_USER or SMTP_PASSWORD not configured in .env"
        print(err_msg)
        return False, err_msg

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"{otp_code} is your Hunar Cycle Academy verification code"
        msg["From"] = f"Hunar Cycle Academy <{user}>"
        msg["To"] = recipient_email

        # Plaintext fallback
        text_content = f"""
Hunar Cycle Academy - Email Verification

Your 6-digit verification code is: {otp_code}

This code expires in 10 minutes.
If you did not request this verification code, please ignore this email.

(c) 2026 Hunar Cycle Academy
"""
        html_content = generate_email_html(otp_code, recipient_email)

        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")
        msg.attach(part1)
        msg.attach(part2)

        # Connect with TLS
        server = smtplib.SMTP(host, port, timeout=25)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, [recipient_email], msg.as_string())
        server.quit()

        print(f"[EmailService] OTP sent successfully to {recipient_email}")
        return True, "Email sent successfully"

    except smtplib.SMTPAuthenticationError as e:
        err_msg = f"[EmailService] SMTP Authentication failed: {e.smtp_error.decode('utf-8', errors='ignore') if hasattr(e, 'smtp_error') else str(e)}"
        print(err_msg)
        return False, err_msg
    except Exception as e:
        err_msg = f"[EmailService] Failed to send email to {recipient_email}: {str(e)}"
        print(err_msg)
        return False, err_msg

def send_otp_email_async(recipient_email: str, otp_code: str):
    """
    Sends email in a background thread to prevent blocking HTTP request lifecycle.
    """
    thread = threading.Thread(
        target=send_otp_email,
        args=(recipient_email, otp_code),
        daemon=True
    )
    thread.start()
    return thread
