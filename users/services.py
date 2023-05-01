from users.models import Users
from users.helpers import is_registered_email
from users.utils import hash_password


def persist_user(name, email, password) -> Users:
    '''
      Persist user with hashed password and 
      return User instance if email are not registerd in
      db, in they case raise Exception
    '''
    if (is_registered_email(email)):
        raise Exception('')

    hashed_password = hash_password(password)
    user = Users(name=name, email=email, password=hashed_password)

    user.save()

    return user
