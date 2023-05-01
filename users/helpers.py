from users.models import Users
from django.core.exceptions import ObjectDoesNotExist


def is_registered_email(email) -> bool:
    try:
        Users.objects.get(email=email)
        return True
    except ObjectDoesNotExist:
        return False
