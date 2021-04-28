from jitsi_connection import generate_link, open_page
from mail_service import send_message


def button_action():
    link = generate_link()
    send_message(link)
    print(link)
    open_page(link)
