
from  email.message import  EmailMessage
from app.config import settings
from pydantic import EmailStr


def create_booking_confirmation_template(
    market_add:dict,
    email_to: EmailStr

):
    email = EmailMessage()

    email["Subject"] = "Подтверждение продажи предмета"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Потверждение Продажи </h1>
            Вы хотите продать за {market_add["price"]}
        """,
        subtype = "html"
    )
    return  email


def create_buying_confirm_template(
        market_buy:dict,
        email_to:EmailStr

):
    email = EmailMessage()

    email["Subject"] = "Подтверждение Покупки предмета"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
                <h1>Вы купили предмет </h1>
                Вы купили предмет за  {market_buy["price"]}
            """,
        subtype="html"
    )
    return email




