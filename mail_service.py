import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from local_auth import sender, password
from network.configurationsGetter import get_mail
import time
import cv2

IMG_NAME = 'photo.png'


def make_photo():
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    cap.set(3, 640)
    cap.set(4, 480)

    if cap.isOpened():
        _, frame = cap.read()
        cap.release()
        if _ and frame is not None:
            cv2.imwrite(IMG_NAME, frame)


def send_message(link: str):
    receiver = get_mail()
    make_photo()
    img_data = open(IMG_NAME, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = "Somebody want to talk"
    msg['From'] = f"Intercom <{sender}>"
    msg['To'] = receiver
    text = MIMEText(f'You can join the talk on intercom on <a href="{link}">link</a>', 'html')
    msg.attach(text)
    image = MIMEImage(img_data, name="photo")
    msg.attach(image)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.close()
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print("Error: unable to send email")
        print(e)
