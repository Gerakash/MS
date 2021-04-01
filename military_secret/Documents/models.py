from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    secret_level = models.CharField(choices=(
        ('public','public'),
        ('private','private'),
        ('secret','secret'),
        ('top_sec','top_sec'),
        ('sup_sec','sup_sec'),
    ),max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=(
        ('active','active'),
        ('dead','dead')
    ),max_length=10,default='active')

