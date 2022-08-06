from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy

# Create your models here.


class UsersTodo(AbstractUser):
    email = models.EmailField(ugettext_lazy('email_address'), unique=True)
