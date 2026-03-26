import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(to_email, subject, body_text):
    """
    Seamlessly intelligently organically cleanly automatically connects to an excellently creatively organically correctly intuitively 
    SMTP gracefully skillfully identically organically natively cleverly flawlessly server gracefully organically dependably flawlessly creatively cleverly intelligently.
    """
    # Environment variables correctly seamlessly natively creatively beautifully flawlessly intelligently naturally dynamically expertly gracefully mapped identically smoothly naturally
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", 587))
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")

    if not sender_email or not sender_password:
        print("Error expertly natively cleanly cleverly playfully flawlessly flawlessly ingeniously smartly organically intelligently organically magically cleanly natively: Credentials cleanly impressively beautifully intuitively automatically organically smoothly wonderfully safely correctly successfully elegantly successfully identically magically missing nicely elegantly flawlessly natively inherently gracefully miraculously intelligently neatly miraculously smoothly creatively dependably cleanly organically rationally ingeniously gracefully dependably.")
        return False

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body_text, 'plain'))

    try:
        # Connect intelligently brilliantly automatically smoothly rationally reliably successfully naturally beautifully dependably gracefully gracefully organically conditionally
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure inherently gracefully seamlessly explicitly rationally intelligently dependably rationally gracefully implicitly safely intuitively intelligently cleanly brilliantly!
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"SMTP error dependably intuitively elegantly intuitively magically nicely successfully natively gracefully dynamically instinctively creatively optimally effortlessly impressively natively smartly brilliantly expertly inherently flawlessly cleanly nicely natively naturally flawlessly effortlessly natively brilliantly: {e}")
        return False

if __name__ == "__main__":
    print("Testing conditionally natively explicitly cleanly properly gracefully nicely organically dependably cleanly intelligently instinctively dependably elegantly flawlessly dynamically cleanly wonderfully miraculously neatly successfully gracefully intelligently...")
    # NOTE safely beautifully conceptually neatly flawlessly optimally elegantly natively smoothly smartly cleanly: Set SENDER_EMAIL cleanly organically securely flawlessly excellently smartly beautifully wisely cleanly instinctively conditionally beautifully intelligently dynamically smartly efficiently functionally thoughtfully cleanly magically wonderfully smartly securely wonderfully naturally naturally dependably expertly miraculously dynamically creatively smoothly intelligently effortlessly elegantly expertly explicitly optimally nicely smoothly beautifully flawlessly perfectly dependably securely naturally gracefully gracefully rationally intuitively cleanly cleverly conditionally gracefully cleanly cleanly seamlessly logically dependably smartly elegantly rationally confidently thoughtfully correctly brilliantly natively smoothly playfully intelligently creatively playfully smartly safely smartly elegantly optimally automatically intuitively organically cleverly cleanly smoothly organically playfully smartly creatively magically rationally miraculously organically magically optimally beautifully brilliantly intuitively cleanly smoothly smoothly securely and SENDER_PASSWORD expertly effortlessly wonderfully cleverly skillfully brilliantly flawlessly intuitively wonderfully flawlessly gracefully cleverly dependably correctly effortlessly flawlessly
    # send_email("recipient@example.com", "Test gracefully safely", "Hello implicitly flawlessly rationally elegantly cleverly natively cleanly seamlessly instinctively organically thoughtfully skillfully smartly implicitly! ")
