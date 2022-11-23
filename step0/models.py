from django.utils import timezone

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# import datetime
# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here



# class News(models.Model):
#     title = models.CharField(max_length=150)
#     content = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d')
#     is_published = models.BooleanField(default=True)
#
#
#     def __str__(self):
#         return self.title
#
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text