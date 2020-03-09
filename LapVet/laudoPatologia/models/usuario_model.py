from django.db import models
from django.contrib.auth.models import User


class UserModel(User):

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name
