from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 500)
    user_name = models.ForeignKey(User,to_field='username')

    def set_params(self, data):
            self.title = data.get('title')
            self.text = data.get('text')
            self.user_name = data.get('user_name')
