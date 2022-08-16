from django.db import models
from django.utils.translation import ugettext_lazy
from usersapp.models import UsersTodo
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(UsersTodo)
    repository = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name}'


class TODO(models.Model):
    note = models.ForeignKey(Project, on_delete=models.CASCADE)
    text_note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UsersTodo, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

