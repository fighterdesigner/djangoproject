
from django.conf import settings
from django.db import models

# Create your models here.
class Question(models.Model):
      question_text = models.CharField(max_length=250)
      pub_date = models.DateTimeField('date published')
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null=True)

      def __str__(self):
          return self.question_text

class Choice(models.Model):
      questions = models.ForeignKey(Question, on_delete = models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)

      def __str__(self):
          return self.choice_text