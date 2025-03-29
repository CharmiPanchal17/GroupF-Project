from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get_by_natural_key(username)

            if not user.is_active:
                raise PermissionDenied("Your account is inactive. Please contact support.")

            if not user.is_verified:
                raise PermissionDenied("Email not verified. Please check your inbox for the verification link.")

            if user.check_password(password):
                return user

            return None

        except User.DoesNotExist:
            return None
