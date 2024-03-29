import requests, json, os, sys
import smtplib, ssl

def handle(req):

    event_header = os.getenv("Http_X_Github_Event")

    if not event_header == "issues":
        sys.exit("Unable to handle X-GitHub-Event: " + event_header)
        return

    gateway_hostname = os.getenv("gateway_hostname", "gateway.openfaas")

    payload = json.loads(req)

    if not payload["action"] == "opened":
        return

    sender_email = "nguyendangto2502@gmail.com"
    sender_password = os.getenv("mail_auth_token")
    receiver_email = "21522685@gm.uit.edu.vn"

    message = f"Subject: You have issue at repo ({payload['issue']['html_url']})\n\n" \
          f"Title:{payload['issue']['title']}\n\n" \
          f"Description: {payload['issue']['body']}"


    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

    return "Email sent with issue body"

    
