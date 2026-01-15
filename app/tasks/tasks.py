import smtplib

from pydantic import EmailStr

from app.config import settings
from app.tasks.celerys import celery
from PIL import Image
from pathlib import Path

from app.tasks.email_templates import create_booking_confirmation_template, create_buying_confirm_template


@celery.task
def process_pic(
        path:str
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_1000_500 = im.resize((1000,500))
    im_resized_200_200 = im.resize((200, 200))
    im_resized_1000_500.save(f"app/static/images/resized_1000_500_{im_path.name}")
    im_resized_200_200.save(f"app/static/images/resized_200_200_{im_path.name}")


@celery.task
def send_market_confirm(
       add_market:dict,
       email_to:EmailStr
):
    email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(add_market,email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)


@celery.task
def send_buy_confirm(
    market_buy:dict,
    email_to:EmailStr

):
    email_to_mock = settings.SMTP_USER
    msg_content = create_buying_confirm_template(market_buy, email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)