import urllib.request
import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PRODUCT_URL = "https://www.superiorshrimpaquatics.com/products/malaysian-trumpet-snail-melanoides-tuberculata.json"
PRODUCT_PAGE = "https://www.superiorshrimpaquatics.com/products/malaysian-trumpet-snail-melanoides-tuberculata"
NOTIFY_EMAIL = "jayolsen@gmail.com"

def check_stock():
    req = urllib.request.Request(PRODUCT_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
    variants = data["product"]["variants"]
    available = [v for v in variants if v["available"]]
    return available

def send_email(available_variants):
    sender = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_APP_PASSWORD"]

    variant_lines = "\n".join(
        f"  - Pack of {v['title']}: ${v['price']}" for v in available_variants
    )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🐚 Malaysian Trumpet Snails are back in stock!"
    msg["From"] = sender
    msg["To"] = NOTIFY_EMAIL

    text = f"""Good news! Malaysian Trumpet Snails are back in stock at Superior Shrimp & Aquatics.

Available pack sizes:
{variant_lines}

Buy now before they sell out:
{PRODUCT_PAGE}
"""

    html = f"""<html><body>
<h2>🐚 Malaysian Trumpet Snails are back in stock!</h2>
<p>Available pack sizes:</p>
<ul>
{"".join(f"<li><strong>Pack of {v['title']}</strong>: ${v['price']}</li>" for v in available_variants)}
</ul>
<p><a href="{PRODUCT_PAGE}" style="background:#1D9E75;color:white;padding:10px 20px;text-decoration:none;border-radius:6px;display:inline-block;">Buy Now →</a></p>
</body></html>"""

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, NOTIFY_EMAIL, msg.as_string())

    print(f"Email sent to {NOTIFY_EMAIL}")

if __name__ == "__main__":
    print("Checking stock...")
    available = check_stock()
    if available:
        print(f"IN STOCK! {len(available)} variant(s) available. Sending email...")
        send_email(available)
    else:
        print("Still sold out. No email sent.")
