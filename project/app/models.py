from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title

class Response(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.body

    def get_responses(self):
        return Response.objects.filter(parent=self)