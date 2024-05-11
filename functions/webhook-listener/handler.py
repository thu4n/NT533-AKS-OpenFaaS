import requests, json, os, sys
import smtplib, ssl

def handle(req):

  event_header = os.getenv("Http_X_Github_Event")

  sender_email = "nguyendangto2502@gmail.com"
  sender_password = os.getenv("mail_auth_token")
  receiver_email = "thuan.tongg@gmail.com"

  if not event_header == "issues":
    sys.exit("Unable to handle X-GitHub-Event: " + event_header)
    return

  payload = json.loads(req)

  message = generate_message(payload)

  with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)

  return "Email sent with issue body"


def generate_message(payload):
  if payload["action"] == "closed":
    return f"Subject: Issue closed at repo ({payload['issue']['html_url']})\n\n" \
           f"Title:{payload['issue']['title']}\n\n" \
           f"Description: The issue have been closed"
  elif payload["action"] == "opened":
    return f"Subject: You have issue at repo ({payload['issue']['html_url']})\n\n" \
           f"Title:{payload['issue']['title']}\n\n" \
           f"Description: {payload['issue']['body']}"
  else:
    return f"Unknown action: {payload['action']}"


    
