from django.db import models
from django.contrib.auth.models import User
#from common.models import User 
# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    star = models.ManyToManyField(User, related_name='stars',blank=True)
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content
    
