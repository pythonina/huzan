from django.contrib.auth.backends import ModelBackend
from django.utils import timezone


class PhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user and not user.is_staff and user.expired <= timezone.now() - timezone.timedelta(seconds=45):
            return None
        return user