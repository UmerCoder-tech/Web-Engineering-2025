
import os
import yagmail
from dotenv import load_dotenv

load_dotenv(dotenv_path="email.env")

ABSENDER_EMAIL = os.getenv("EMAIL_USER")
APP_PASSWORT = os.getenv("EMAIL_PASSWORD")

def sende_bestaetigungs_email(empfaenger_email, status, bewerbername):
    # KEIN alias hier!
    yag = yagmail.SMTP(user=ABSENDER_EMAIL, password=APP_PASSWORT)

    if status == "angenommen":
        betreff = "Ihre Bewerbung bei der Nord Academy"
        inhalt = f"""
        <h2>Herzlichen Glückwunsch, {bewerbername}!</h2>
        <p>Ihre Bewerbung bei der <strong>Nord Academy</strong> wurde <span style="color:green;"><strong>angenommen</strong></span>.</p>
        <p>Wir freuen uns, Sie bald bei uns begrüßen zu dürfen.</p>
        <hr>
        <p style="font-size:12px;color:gray;">Diese Nachricht wurde automatisch versendet. Bitte nicht antworten.</p>
        """
    else:
        betreff = "Ihre Bewerbung bei der Nord Academy"
        inhalt = f"""
        <h2>Hallo {bewerbername},</h2>
        <p>Leider müssen wir Ihnen mitteilen, dass Ihre Bewerbung bei der <strong>Nord Academy</strong> <span style="color:red;"><strong>abgelehnt</strong></span> wurde.</p>
        <p>Wir bedanken uns dennoch für Ihr Interesse und wünschen Ihnen für Ihre Zukunft alles Gute.</p>
        <hr>
        <p style="font-size:12px;color:gray;">Diese Nachricht wurde automatisch versendet. Bitte nicht antworten.</p>
        """

    try:
        yag.send(
            to=empfaenger_email,
            subject=betreff,
            contents=[inhalt],
        )
    except Exception as e:
        print(f"Fehler beim Mailversand: {e}")
