from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
import datetime

def send_verification_email(user, request=None):
    """
    Sends an email verification link to the user.
    The link expires in 24 hours.
    """
    token = jwt.encode(
        {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

    domain = get_current_site(request).domain if request else settings.FRONTEND_URL
    protocol = "https" if not settings.DEBUG else "http"
    verification_url = f"{protocol}://{domain}/api/auth/verify/{token}/"

    subject = "Verify Your Account"
    message = (
        f"Hi {user.get_full_name() or user.email},\n\n"
        f"Click the link below to verify your account:\n"
        f"{verification_url}\n\n"
        f"This link expires in 24 hours.\n\n"
        f"If you didn't request this, please ignore this email."
    )

    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
