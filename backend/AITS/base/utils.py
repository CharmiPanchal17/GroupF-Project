from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
import datetime

def send_verification_email(user, request):
    token = jwt.encode(
        {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )
    
    verification_url = f"http://{get_current_site(request).domain}/api/auth/verify/{token}/"
    
    subject = "Verify Your Account"
    message = f"Hi {user.username},\n\nClick the link below to verify your account:\n{verification_url}\n\nThis link expires in 24 hours."
    
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
