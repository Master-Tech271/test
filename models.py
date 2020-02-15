from django.db import models
from django.contrib.auth import get_user_model,login,logout
from django.conf import settings
import uuid,os
# Create your models here.

def path_and_rename(prefix, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join(prefix, filename)

# Home model stuff
def Question_image(instance, filename):
    return path_and_rename('drivingtest/question', filename)

def Option_image(instance, filename):
    return path_and_rename('drivingtest/option', filename)


class TestUser(models.Model):
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    uid = models.CharField(max_length=255, blank=True, unique=True, default=uuid.uuid4)

# class Test_Q(models.Model):
#     testuser=models.ForeignKey(TestUser,on_delete=models.CASCADE)
#     uid = models.TextField()
#     is_true=models.BooleanField(default=False)

class Question(models.Model):
    question=models.TextField(max_length=1000)
    image = models.FileField(upload_to=Question_image,null=True,blank=True)
    uid = models.CharField(max_length=255, blank=True, unique=True, default=uuid.uuid4)
    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    text = models.TextField(default="text")
    image = models.FileField(upload_to=Option_image,null=True,blank=True)
    uid = models.CharField(max_length=255, blank=True, unique=True, default=uuid.uuid4)
