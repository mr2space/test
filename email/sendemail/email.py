from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
import threading
import magic



class SendEmailThread(threading.Thread):
    def __init__(self,email,img):
        self.email = email
        self.img = img
        threading.Thread.__init__(self)

    def run(self):
        temp = "email_template.html"
        try:
            html = get_template(temp)
            html_content = html.render()
            subject = f"Python (Selenium) Assignment - Prince Goswami"
            from_email = "princegoswami.space@gmail.com"
            to = self.email
            print("prepraied")
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            print("attachment")
            file_content = self.img.read()
            mime_type = magic.from_buffer(file_content, mime=True)
            msg.attach("img",file_content, mime_type)
            print("Sending mail")
            msg.send()
        except Exception as error:
            print("Error in sending the email", error, error.with_traceback)
            return -1
        return 0